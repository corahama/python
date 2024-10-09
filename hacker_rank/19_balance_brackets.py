#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

op = ['{', '[', '(']
cl = ['}', ']', ')']

def isBalanced(s):
    if len(s) % 2 != 0: return 'NO'

    chrs = []

    for c in s:
        if c in op:
            chrs.append(c)
        elif len(chrs) == 0:
            return 'NO'
        elif chrs.pop() != op[cl.index(c)]:
            return 'NO'

    return 'YES' if len(chrs) == 0 else 'NO'

if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", "(2).txt", os.path.basename(__file__))}', 'r')

    # f = open('g_output.txt', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)
        # f.write(result+'\n')

    # f.close()