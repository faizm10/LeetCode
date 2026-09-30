"""
p28. Random Pick with Weight (Medium)
Topic: Prefix Sums / Binary Search
Known as a frequently-asked Google interview question.

You're given an array of positive weights w, where w[i] describes the
weight of index i. Implement pick_index() so that the probability of
picking index i is w[i] / sum(w).

To keep this testable offline (no statistics needed): pick_index accepts
an optional rand_val in [0, 1). If omitted it defaults to random.random().
Given a rand_val, the mapping onto an index via prefix sums is
deterministic, so tests can pass fixed rand_vals and assert exact indices.

Example:
w = [1, 3]  -> prefix sums [1, 4], total = 4
  rand_val=0.1 -> target=0.4 -> falls in [0, 1) -> index 0
  rand_val=0.5 -> target=2.0 -> falls in [1, 4) -> index 1
"""

import random


class Solution:
    def __init__(self, w):
        self.prefix = []
        total = 0
        for x in w:
            total += x
            self.prefix.append(total)
        self.total = total

    def pick_index(self, rand_val=None):
        if rand_val is None:
            rand_val = random.random()
        target = rand_val * self.total
        lo, hi = 0, len(self.prefix) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self.prefix[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    sol = Solution([1, 3])
    assert sol.pick_index(0.1) == 0
    assert sol.pick_index(0.5) == 1
    assert sol.pick_index(0.9) == 1

    sol2 = Solution([1])
    assert sol2.pick_index(0.5) == 0

    # default rand_val (no argument) should still return a valid index
    assert sol.pick_index() in (0, 1)
    print("All tests passed!")
