#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#


# limit time 10 s
def truckTour(petrolpumps):
    petrolpumps = list(map(lambda p: p[0]-p[1], petrolpumps))
    p_len = len(petrolpumps)

    tank, s_idx, i, path_count = 0, 0, 0, 0
    while path_count < p_len:
        tank += petrolpumps[i%p_len]
        if tank < 0:
            while tank < 0:
                tank -= petrolpumps[s_idx]
                s_idx += 1
                path_count -= 1
        i += 1
        path_count += 1

    return s_idx


if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    print(result)