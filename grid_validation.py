import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
grid = []

def validate_grid(grid):
    for ii in range(9):
        column = []
        for jj in range(9):
            if grid[ii].count(jj+1) > 1:
                return "false"
            if grid[jj][ii] in column:
                return "false"
            column.append(grid[jj][ii])


    for row in [0,3,6]:
        for col in [0,3,6]:
            soduku_subgrid=[]
            for i in range(0,3):
                for j in range(0,3):
                    if grid[row+i][col+j] in soduku_subgrid:
                        return "false"
                    soduku_subgrid.append(grid[row+i][col+j])
    return "true"

for i in range(9):
    soduku_grid_line = []
    for j in input().split():
        n = int(j)
        soduku_grid_line.append(n)
    grid.append(soduku_grid_line)

answer = (validate_grid(grid))
print(answer)
