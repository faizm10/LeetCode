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
    """
    sorted_nums = [-4,-1,-1,0,1,2]
    l = -1
    r = 2
    i = -4

    we would wanna start with the index of the loop and use two points to iterate the ones on the left side and right side while skipping duplicates as well

    so first we would stary with the first index of nums, use l to go thru on the left and use r to go on the right. 
    """
    
    
   


def _normalize(triplets):
    return sorted(sorted(t) for t in triplets)


if __name__ == "__main__":
    assert _normalize(three_sum([-1, 0, 1, 2, -1, -4])) == _normalize([[-1, -1, 2], [-1, 0, 1]])
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    print("All tests passed!")
