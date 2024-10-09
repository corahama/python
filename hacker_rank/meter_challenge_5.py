#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'matchingBraces' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY braces as parameter.
#

op = ['{', '[', '(']
cl = ['}', ']', ')']

def matchingBraces(braces):
    results = []
    for s in braces:
        results.append(isBalanced(s))
    return results

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
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    braces_count = int(input().strip())

    braces = []

    for _ in range(braces_count):
        braces_item = input()
        braces.append(braces_item)

    result = matchingBraces(braces)

    print(result)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
