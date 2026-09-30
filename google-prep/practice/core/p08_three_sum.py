"""
p08. 3Sum (Medium)
Topic: Two Pointers / Sorting

Given an integer array nums, return all unique triplets [a, b, c] such
that a + b + c == 0. The solution set must not contain duplicate triplets.
Order of triplets, and order within a triplet, does not matter.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""


def three_sum(nums):
    # TODO: implement
    pass


def _normalize(triplets):
    return sorted(sorted(t) for t in triplets)


if __name__ == "__main__":
    assert _normalize(three_sum([-1, 0, 1, 2, -1, -4])) == _normalize([[-1, -1, 2], [-1, 0, 1]])
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    print("All tests passed!")
