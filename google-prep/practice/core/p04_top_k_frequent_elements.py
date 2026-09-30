"""
p04. Top K Frequent Elements (Medium)
Topic: Arrays / Heap

Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""


def top_k_frequent(nums, k):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(top_k_frequent([1], 1)) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 5, 5, 6], 2)) == [4, 5]
    assert sorted(top_k_frequent([1, 2, 3], 3)) == [1, 2, 3]
    print("All tests passed!")
