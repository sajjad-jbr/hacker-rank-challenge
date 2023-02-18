#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    res=0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            val = grid[row][col]
            flag = 1
            for rr in range (max(0,row-1),min(len(grid),row+2)):
                for cc in range(max(0,col-1),min(len(grid[0]),col+2)):
                    if (rr,cc)!=(row,col) and val<= grid[rr][cc] :
                         flag=0
                         break 
                if flag == 0:
                     break
            else:
                res+=1
    return res;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
