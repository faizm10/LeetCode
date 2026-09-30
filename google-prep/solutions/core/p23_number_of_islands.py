"""
p23. Number of Islands (Medium)
Topic: Graphs / BFS-DFS

Given a 2D grid of '1' (land) and '0' (water), return the number of
islands. An island is surrounded by water and formed by connecting
adjacent lands horizontally or vertically.

Example:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from collections import deque


def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = cr + dr, cc + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and not visited[nr][nc]
                    and grid[nr][nc] == "1"
                ):
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:
                count += 1
                bfs(r, c)

    return count


if __name__ == "__main__":
    assert num_islands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]) == 3
    assert num_islands([
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"],
    ]) == 1
    assert num_islands([["0"]]) == 0
    assert num_islands([["1"]]) == 1
    print("All tests passed!")
