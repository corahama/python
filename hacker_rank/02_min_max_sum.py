#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_n, max_n = arr[0], arr[0]

    for i, n in enumerate(arr):
        if n < min_n:
            min_n = n
        elif n > max_n:
            max_n = n

    num_sum = sum(arr)
    print(f'{num_sum-max_n} {num_sum-min_n}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
