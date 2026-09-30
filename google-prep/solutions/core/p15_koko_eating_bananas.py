"""
p15. Koko Eating Bananas (Medium)
Topic: Binary Search on Answer

Koko has piles of bananas and h hours. Each hour she picks one pile and
eats up to k bananas from it (if the pile has fewer than k, she finishes
the pile and stops for that hour). Find the minimum integer eating speed k
such that she can eat all bananas within h hours.

Example:
Input: piles = [3,6,7,11], h = 8
Output: 4
"""

import math


def _hours_needed(piles, speed):
    return sum(math.ceil(p / speed) for p in piles)


def min_eating_speed(piles, h):
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if _hours_needed(piles, mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    assert min_eating_speed([1000000000], 2) == 500000000
    print("All tests passed!")
