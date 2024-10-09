#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxTrailing' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY levels as parameter.
#


def maxTrailing(levels):
    print(len([l for l in levels if l<0]))
    if len([l for l in levels if l>0]) > 0:
        high_i = levels.index(max(levels))
        if high_i == 0: return -1

        lowest = min(levels[:high_i])
        return levels[high_i]-lowest

    else:
        high_i = levels.index(min(levels))
        if high_i == 0: return -1

        lowest = max(levels[high_i:])
        return abs(levels[high_i]-lowest)


if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    levels_count = int(input().strip())

    levels = []

    for _ in range(levels_count):
        levels_item = int(input().strip())
        levels.append(levels_item)

    result = maxTrailing(levels)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
