"""
p07. Two Sum II - Input Array Is Sorted (Medium)
Topic: Two Pointers

Given a 1-indexed array of integers `numbers` sorted in ascending order,
find two numbers that add up to `target`. Return their 1-indexed positions
as [index1, index2] with index1 < index2. Aim for O(n) time, O(1) space.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
"""


def two_sum_ii(numbers, target):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert two_sum_ii([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_ii([2, 3, 4], 6) == [1, 3]
    assert two_sum_ii([-1, 0], -1) == [1, 2]
    assert two_sum_ii([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
    print("All tests passed!")
