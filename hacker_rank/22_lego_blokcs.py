#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#



def tetranacci(n): 
    arr = [1, 2, 4, 8]
    if n <= 4: 
        return arr[:n]
    else: 
        for i in range(4, n):
            arr.append(sum(arr[i-4:i])%(10**9 + 7))
    return arr

# n = height, m = weight
def legoBlocks(n, m):
    MOD = (10**9 +7)
    a, s = [(v**n)%MOD for v in tetranacci(m)], [1]

    for i in range(1, len(a)):
        sums = sum([x*y for x,y in zip(a[:i], s[::-1])])
        s.append( (a[i]-sums)%MOD)
    return s[-1]


if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    t = int(input().strip())

    for t_itr in range(t):
        # first_multiple_input = input().rstrip().split()

        # n = int(first_multiple_input[0])

        # m = int(first_multiple_input[1])

        n, m = list(map(int, input().rstrip().split()))

        result = legoBlocks(n, m)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()

# Combinations
# n!/(r!*(n-r)!)

# Permutations
# repiting: n^r
# non-repeting: n!/(n-r)!