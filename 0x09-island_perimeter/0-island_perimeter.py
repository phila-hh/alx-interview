#!/usr/bin/python3
"""
0-island_perimeter module
"""


def island_perimeter(grid):
    """ Returns the perimeter of island """
    perimeter = 0
    if type(grid) is list:
        x = len(grid)
        for i, row in enumerate(grid):
            y = len(row)
            for j, cell in enumerate(row):
                if cell == 0:
                    continue
                sides = (
                    i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                    j == y - 1 or (y > j + 1 and row[j + 1] == 0),
                    i == x - 1 or (len(grid[i + 1]) > j and
                                   grid[i + 1][j] == 0),
                    j == 0 or row[j - 1] == 0,
                )
                perimeter += sum(sides)
    return perimeter
