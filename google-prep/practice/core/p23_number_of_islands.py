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


def num_islands(grid):
    # TODO: implement
    pass


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
