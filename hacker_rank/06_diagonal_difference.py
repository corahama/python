#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    num_1, num_2 = 0, 0
    for i in range(len(arr)):
        num_1 += arr[i][i]
        num_2 += arr[-i-1][i]

    return abs(num_1-num_2)

if __name__ == '__main__':
    sys.stdin = open(re.sub('.py', '.txt', f'test_cases/{os.path.basename(__file__)}'), 'r')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)