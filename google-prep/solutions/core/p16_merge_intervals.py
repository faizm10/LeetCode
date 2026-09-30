"""
p16. Merge Intervals (Medium)
Topic: Intervals / Sorting

Given an array of intervals [start, end], merge all overlapping intervals
and return an array of the non-overlapping intervals that cover all the
intervals in the input, sorted by start.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""


def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda iv: iv[0])
    merged = [intervals[0][:]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


if __name__ == "__main__":
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([]) == []
    assert merge_intervals([[1, 4]]) == [[1, 4]]
    print("All tests passed!")
