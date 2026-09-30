"""
p17. Insert Interval (Medium)
Topic: Intervals

You are given a list of non-overlapping intervals sorted by start, and a
new interval. Insert the new interval, merging as needed, and return the
resulting sorted, non-overlapping list of intervals.

Example:
Input: intervals = [[1,3],[6,9]], new_interval = [2,5]
Output: [[1,5],[6,9]]
"""


def insert_interval(intervals, new_interval):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert_interval(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    ) == [[1, 2], [3, 10], [12, 16]]
    assert insert_interval([], [5, 7]) == [[5, 7]]
    assert insert_interval([[1, 5]], [2, 3]) == [[1, 5]]
    print("All tests passed!")
