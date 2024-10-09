#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

import queue

def bfs(n, m, edges, s):
    graph = [[0]*n for _ in range(n)]
    distances = [-1]*n

    q = queue.Queue()

    for edge in edges:
        graph[edge[0]-1][edge[1]-1] = graph[edge[1]-1][edge[0]-1] = 1

    q.put(s - 1)
    distances[s - 1] = 0
    
    while not q.empty():
        a = q.get()
        for j in range(n):
            if graph[a][j] and distances[j] < 0:
                q.put(j)
                distances[j] = distances[a] + 6

    return distances[:s-1]+distances[s:]


if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)
        print(result)

        map(int, input().rstrip().split())