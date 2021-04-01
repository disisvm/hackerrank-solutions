#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort()
    a = len(arr) // 2
    L = arr[:a]
    H = arr[-a:]
    Q1 = int(statistics.median(L))
    Q2 = int(statistics.median(arr))
    Q3 = int(statistics.median(H))
    return Q1,Q2,Q3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
