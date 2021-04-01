#!/bin/python3

import math
import os
import random
import re
import sys
import statistics
#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    m = statistics.mean(arr)
    c = 0
    for i in arr:
        c += ((i-m)**2)
    print("{:.1f}".format((c/len(arr))**(0.5)))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
