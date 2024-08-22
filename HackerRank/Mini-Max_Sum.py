#!/bin/python3

import math
import os
import random
import re
import sys

#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.


# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    maximum = 0
    minimum = 0
    
    for i in arr:
        maximum += i
        minimum += i
        
    minimum -= max(arr)
    maximum -= min(arr)
    print(f"{minimum} {maximum}")