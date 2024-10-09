#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    i = len(q)
    bribe = 0

    while i > 0:
        if q[i-1] != i:
            if q[i-2] == i:
                q[i-2], q[i-1] = q[i-1], q[i-2]
                bribe += 1
            elif q[i-3] == i:
                q[i-3], q[i-2] = q[i-2], q[i-3]
                q[i-2], q[i-1] = q[i-1], q[i-2]
                bribe += 2
            else:
                print('Too chaotic')
                return
        i -= 1

    print(bribe)


if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    t = int(input().strip())

    from time import time
    start = time()
    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
    print('time spent: ', time()-start)