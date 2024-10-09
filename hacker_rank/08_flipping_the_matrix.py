#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    t_sum = 0
    for i in range(len(matrix)//2):
        for j in range(len(matrix)//2):
            if matrix[i][-j-1] > matrix[i][j]:
                matrix[i][j] = matrix[i][-j-1]
            if matrix[-i-1][j] > matrix[i][j]:
                matrix[i][j] = matrix[-i-1][j]
            if matrix[-i-1][-j-1] > matrix[i][j]:
                matrix[i][j] = matrix[-i-1][-j-1]
            t_sum += matrix[i][j]

    return t_sum

if __name__ == '__main__':
    sys.stdin = open(re.sub('.py', '.txt', f'test_cases/{os.path.basename(__file__)}'), 'r')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print(result)

