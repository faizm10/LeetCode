"""
p24. Course Schedule (Medium)
Topic: Graphs / Topological Sort

There are num_courses courses labeled 0..num_courses-1. prerequisites[i] =
[a, b] means you must take course b before course a. Return True if it is
possible to finish all courses (i.e. the prerequisite graph has no cycle).

Example:
Input: num_courses = 2, prerequisites = [[1,0]]
Output: True

Input: num_courses = 2, prerequisites = [[1,0],[0,1]]
Output: False
"""


def can_finish(num_courses, prerequisites):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(1, []) is True
    assert can_finish(3, [[1, 0], [2, 1]]) is True
    assert can_finish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]) is False
    print("All tests passed!")
