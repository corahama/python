#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
# n = number of towers, m = height of towers
def towerBreakers(n, m):
    return 2 if (not n%2 or m==1) else 1


if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        print(result)