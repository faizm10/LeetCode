"""
p04. Top K Frequent Elements (Medium)
Topic: Arrays / Heap

Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""


from collections import Counter
from typing import List

def top_k_frequent(nums, k):
    # Step 1: Count the frequency of each element
    frequency = Counter(nums)
    # prints out {1:3, 2:2, 3:1}
    sorted_elements = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    #freq.items() = turns from dict to tuples so like (1,3),(2,3) etc
    #key=lambda x: x[1] = x[1] returns the 2nd element of each tuples
    top_k_elements = [element[0] for element in sorted_elements[:k]]
    # goes into the tuples and return the first x elements
    return top_k_elements

if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(top_k_frequent([1], 1)) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 5, 5, 6], 2)) == [4, 5]
    assert sorted(top_k_frequent([1, 2, 3], 3)) == [1, 2, 3]
    print("All tests passed!")
