#!/bin/python3

import math
import os
import random
import re
import sys


# Given an array of integers, where all elements but one occur twice, find the unique element.


# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    unique = 0
    for num in a:
        unique ^= num
    return unique

    
    