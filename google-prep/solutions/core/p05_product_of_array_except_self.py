"""
p05. Product of Array Except Self (Medium)
Topic: Arrays / Prefix-Suffix

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all elements of nums except nums[i]. Do this in
O(n) time without using division, and without counting the output array
toward extra space (O(1) extra space is achievable).

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""


def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([2, 3]) == [3, 2]
    print("All tests passed!")
