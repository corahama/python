#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    num = str(sum(map(lambda n: int(n), n)))*k
    while len(num) > 1:
        num = str(sum(map(lambda n: int(n), num)))

    return num

if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    # first_multiple_input = input().rstrip().split()

    # n = first_multiple_input[0]

    # k = int(first_multiple_input[1])

    n = str(random.randint(10**100000,10**100000))
    k = 10**5

    result = superDigit(n, k)

    print(result)