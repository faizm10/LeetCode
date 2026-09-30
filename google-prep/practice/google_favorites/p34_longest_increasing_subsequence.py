"""
p34. Longest Increasing Subsequence (Medium)
Topic: Dynamic Programming
Known as a frequently-asked Google interview question.

Given an integer array nums, return the length of the longest strictly
increasing subsequence (elements need not be contiguous). Aim for
O(n log n), though an O(n^2) DP solution is also acceptable to practice
first.

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4   (the subsequence [2,3,7,18] or [2,3,7,101])
"""


def length_of_lis(nums):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7]) == 1
    assert length_of_lis([]) == 0
    assert length_of_lis([1, 2, 3, 4]) == 4
    print("All tests passed!")
