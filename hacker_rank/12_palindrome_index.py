#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def palindromeIndex(s):
    c_idx = None
    l_offset, r_offset = 0, 0

    for i in range(math.ceil(len(s)/2)):
        if s[i+l_offset] != s[-i-1-r_offset]:
            if r_offset:
                return -1
            if l_offset:
                i = c_idx
                if s[i+1] == s[-i-1]:
                    l_offset, r_offset = 0, 1
                    c_idx = len(s)-1-i
                continue
            if s[i+1] == s[-i-1]:
                l_offset += 1
                c_idx = i
            elif s[i] == s[-i-2]:
                r_offset += 1
                c_idx = len(s)-1-i
            else:
                return -1

    return -1 if (not l_offset and not r_offset) else c_idx


if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(result)