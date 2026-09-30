"""
p26. Meeting Rooms II (Medium)
Topic: Heaps / Intervals
Known as a frequently-asked Google interview question.

Given an array of meeting time intervals [start, end], return the minimum
number of conference rooms required so no two overlapping meetings share a
room.

Example:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
"""

import heapq


def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda iv: iv[0])
    heap = []  # end times of rooms currently in use

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)

    return len(heap)


if __name__ == "__main__":
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([]) == 0
    assert min_meeting_rooms([[1, 5], [5, 10]]) == 1
    assert min_meeting_rooms([[1, 10], [2, 7], [3, 19]]) == 3
    print("All tests passed!")
