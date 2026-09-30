"""
p09. Container With Most Water (Medium)
Topic: Two Pointers

Given n non-negative integers `height` where each represents a vertical
line at index i, find two lines that together with the x-axis form a
container that holds the most water. Return the maximum area.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
"""


def max_area(height):
    lo, hi = 0, len(height) - 1
    best = 0
    while lo < hi:
        area = (hi - lo) * min(height[lo], height[hi])
        best = max(best, area)
        if height[lo] < height[hi]:
            lo += 1
        else:
            hi -= 1
    return best


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    print("All tests passed!")
