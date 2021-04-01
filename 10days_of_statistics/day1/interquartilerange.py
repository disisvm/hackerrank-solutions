#!/bin/python3

import math
import os
import random
import re
import sys
import statistics
#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = []
    for i in range(len(values)):
        arr.extend([values[i]]*freqs[i])
    arr.sort()
    a = len(arr) // 2
    L = arr[:a]
    H = arr[-a:]
    Q1 = statistics.median(L)
    Q3 = statistics.median(H)
    print("{:.1f}".format(Q3-Q1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
