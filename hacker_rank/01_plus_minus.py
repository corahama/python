#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    l_than_z, g_than_z, z = [0]*3
    
    for n in arr:
        if n < 0:
            l_than_z += 1
        elif n > 0:
            g_than_z += 1
        else:
            z += 1
    
    print(f'{g_than_z/len(arr):.6f}\n{l_than_z/len(arr):.6f}\n{z/len(arr):.6f}')
            
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
