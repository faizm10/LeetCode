"""
p01. Contains Duplicate (Easy)
Topic: Arrays / Hashing

Given an integer array nums, return True if any value appears at least
twice in the array, and False if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: True
"""


def contains_duplicate(nums):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([]) is False
    assert contains_duplicate([1]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    print("All tests passed!")
