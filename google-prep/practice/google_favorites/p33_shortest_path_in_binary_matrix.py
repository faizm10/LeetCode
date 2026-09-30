"""
p33. Shortest Path in Binary Matrix (Medium)
Topic: BFS / Grids
Known as a frequently-asked Google interview question.

Given an n x n binary grid where 0 = open cell and 1 = blocked cell,
return the length (number of cells visited, including start and end) of
the shortest clear path from top-left to bottom-right, moving in any of
the 8 directions (including diagonals). Return -1 if no such path exists.

Example:
Input: grid = [[0,1],[1,0]]
Output: 2
"""

from collections import deque


def shortest_path_binary_matrix(grid):
    # TODO: implement
    pass


if __name__ == "__main__":
    assert shortest_path_binary_matrix([[0, 1], [1, 0]]) == 2
    assert shortest_path_binary_matrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert shortest_path_binary_matrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    assert shortest_path_binary_matrix([[0]]) == 1
    assert shortest_path_binary_matrix([[1]]) == -1
    print("All tests passed!")
