# Quicksort usually has a running time of n * log(n), but is there an algorithm that can sort even faster? In general, this is not possible. 
# Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. 
# A comparison sort algorithm cannot beat n * log(n) (worst-case) running time, since n * log(n) represents the minimum number of 
# comparisons needed to know where to place each element. For more details, you can see these notes (PDF).

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    
    new_arr = [0] * 100
    
    for i in arr:
        new_arr[i] += 1 

if __name__ == '__main__':
    arr = [1,1,3,2,1]
    result = countingSort(arr)
    print(result)
    
