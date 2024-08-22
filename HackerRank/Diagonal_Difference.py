
#!/bin/python3

import math
import os
import random
import re
import sys

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# 1 2 3
# 4 5 6
# 7 8 9
# 1+5+9 = [0][0] + [1][1]+[2][2]
# 1+5+9 = [2][0] + [1][1]+[0][2]
def diagonalDifference(arr):
    r_to_l = 0
    l_to_r = 0
    
    n = len(arr)  # Get the size of the matrix (number of rows)
    
    for i in range(n):
        r_to_l += arr[i][i]         # Sum for the primary diagonal
        l_to_r += arr[i][n - 1 - i]  # Sum for the secondary diagonal
    
    return abs(r_to_l - l_to_r)
            