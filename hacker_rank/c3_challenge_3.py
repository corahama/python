#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

combs = {
    'a': ['e'],
    'e': ['a', 'i'],
    'i': ['a', 'e', 'o', 'u'],
    'o': ['i', 'u'],
    'u': ['a']
}

def countPerms(n):
    count = { 'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1 }

    for _ in range(1, n):
        t_count = {k:0 for k in count.keys()}
        for k in count.keys():
            for l in combs[k]:
                t_count[l] += count[k]
        count = t_count

    return sum(count.values()) % (10**9+7)

def countPerms2(n):
    nodes = ['a', 'e', 'i', 'o', 'u']

    for _ in range(1, n):
        nodes = [letters for l in nodes for letters in combs[l]]
    
    return len(nodes) % (10**9+7)

def countPermsRecursive(n):
    count = [0]

    for l in combs.keys():
        construct_path(l, n, count)

    return count[0] % (10**9+7)
def construct_path(s, n, count):
    if len(s) < n:
        for l in combs[s[-1]]:
            construct_path(s+l, n, count)
    else:
        count[0] += 1
        return


if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    n = int(input().strip())

    from time import time

    start = time()
    # result = countPermsRecursive(n)
    result = countPerms(n)

    print(result)
    print('taken time: ', time()-start)
    # fptr.write(str(result) + '\n')

    # fptr.close()
