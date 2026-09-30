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
    n = len(grid)
    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    queue = deque([(0, 0, 1)])
    visited = {(0, 0)}

    while queue:
        r, c, dist = queue.popleft()
        if r == n - 1 and c == n - 1:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1


if __name__ == "__main__":
    assert shortest_path_binary_matrix([[0, 1], [1, 0]]) == 2
    assert shortest_path_binary_matrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert shortest_path_binary_matrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    assert shortest_path_binary_matrix([[0]]) == 1
    assert shortest_path_binary_matrix([[1]]) == -1
    print("All tests passed!")
