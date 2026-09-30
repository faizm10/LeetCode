"""
p14. Search in Rotated Sorted Array (Medium)
Topic: Binary Search

An ascending array of distinct integers was rotated at some unknown pivot.
Given the rotated array and a target, return its index, or -1 if not
found. Must run in O(log n).

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""


def search_rotated(nums, target):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
    assert search_rotated([1], 1) == 0
    assert search_rotated([5, 1, 3], 5) == 0
    print("All tests passed!")
