"""
p31. Kth Largest Element in an Array (Medium)
Topic: Heaps / Quickselect
Known as a frequently-asked Google interview question.

Given an integer array nums and an integer k, return the kth largest
element (the kth largest in sorted order, not the kth distinct element).

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""


def find_kth_largest(nums, k):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
    assert find_kth_largest([2, 1], 2) == 1
    print("All tests passed!")
