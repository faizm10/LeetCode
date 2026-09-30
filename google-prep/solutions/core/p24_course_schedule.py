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

from collections import defaultdict, deque


def can_finish(num_courses, prerequisites):
    adj = defaultdict(list)
    in_degree = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        in_degree[a] += 1

    queue = deque(c for c in range(num_courses) if in_degree[c] == 0)
    visited = 0
    while queue:
        c = queue.popleft()
        visited += 1
        for nxt in adj[c]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return visited == num_courses


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(1, []) is True
    assert can_finish(3, [[1, 0], [2, 1]]) is True
    assert can_finish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]) is False
    print("All tests passed!")
