#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    k = k % 26
    cipher_str = []
    for c in map(lambda c: ord(c), s):
        if 65 <= c <= 90:
            cipher_str.append(chr(65+(c+k-65)%26))
        elif 97 <= c <= 122:
            cipher_str.append(chr(97+(c+k-97)%26))
        else:
            cipher_str.append(chr(c))

    return "".join(cipher_str)

if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)