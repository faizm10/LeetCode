#!/bin/python3
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# #Print the decimal value of each fraction on a new line with 6 places after the decimal.


import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    total = len(arr)

    for i in arr:
        if i < 0:
            n += 1
        elif i > 0:
            p += 1
        else:
            z += 1
            
    print(f"{p/total:.6f}") 
    print(f"{n/total:.6f}") 
    print(f"{z/total:.6f}") 
    