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
    res_arr = [0]*100

    for e in arr:
        res_arr[e] += 1
    
    return res_arr

if __name__ == '__main__':
    sys.stdin = open(re.sub('.py', '.txt', f'test_cases/{os.path.basename(__file__)}'), 'r')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(result)