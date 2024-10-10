#!/usr/bin/python3
"""island_perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                # check left
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # check right
                if col == len(grid[row]) - 1 or grid[row][col+1] == 0:
                    perimeter += 1
                # check up
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # check down
                if row == len(grid) - 1 or grid[row+1][col] == 0:
                    perimeter += 1

    return perimeter
