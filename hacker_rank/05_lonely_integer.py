#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    result = 0

    for e in a:
        result ^= e

    return result

if __name__ == '__main__':
    sys.stdin = open(re.sub('.py', '.txt', f'test_cases/{os.path.basename(__file__)}'), 'r')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)
