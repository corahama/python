#!/bin/python3

import math
import os
import random
import re
import sys


S = ""
HISTORY = []

def process_command(t, arg=None):
    global S

    if t == '1':
        HISTORY.append(str(S))
        S += arg
    elif t == '2':
        HISTORY.append(str(S))
        S = S[:len(S)-int(arg)]
    elif t == '3':
        print(S[int(arg)-1])
    elif t == '4':
        S = str(HISTORY[-1])
        HISTORY.pop()
    else:
        raise Exception("command invalid")


if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    Q = int(input().rstrip())

    for _ in range(Q):
        inp = input().rstrip().split()
        process_command(*inp)
