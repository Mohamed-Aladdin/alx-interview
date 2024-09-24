#!/usr/bin/python3
"""Island Perimeter Problem Module
"""

from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """Returns the perimeter of the island described in grid
    """
    checked = set()

    def dfs(i: int, j: int) -> int:
        """Depth first search algorithm
        """
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 \
                or grid[i][j] == 0:
            return 1
        if (i, j) in checked:
            return 0
        checked.add((i, j))
        perimeter = dfs(i, j + 1)
        perimeter += dfs(i + 1, j)
        perimeter += dfs(i, j - 1)
        perimeter += dfs(i - 1, j)

        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
