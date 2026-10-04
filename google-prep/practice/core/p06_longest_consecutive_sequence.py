"""
p06. Longest Consecutive Sequence (Medium)
Topic: Arrays / Hashing

Given an unsorted array of integers, return the length of the longest run
of consecutive integers (values, not indices). Must run in O(n) time.

Example:
Input: nums = [100,4,200,1,3,2]
Output: 4   (the sequence is 1,2,3,4)
"""


from numpy import empty, sort

def longest_consecutive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    max_length = 0
    for num in nums:
        print(str(num) + " num")
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length

if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1, 2, 0, 1]) == 3
    assert longest_consecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7
    print("All tests passed!")
