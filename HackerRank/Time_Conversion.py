#!/bin/python3

import math
import os
import random
import re
import sys

# Given a 12- time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = s.split(':')
    if (s[-2:] == "PM" ) and (s[0:2] != "12"):
        return f"{int(time[0]) + 12}{s[2:-2]}"
    elif (s[-2:] == "AM" ) and (s[0:2] == "12"):
        return f"{s[2:-2]:0>{8}}"
    else:
        return s[:-2]
