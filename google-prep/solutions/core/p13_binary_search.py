"""
p13. Binary Search (Easy)
Topic: Binary Search

Given a sorted (ascending) array of distinct integers `nums` and a target
value, return the index of target if it exists, else -1. O(log n).

Example:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
"""


def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([], 5) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    print("All tests passed!")
