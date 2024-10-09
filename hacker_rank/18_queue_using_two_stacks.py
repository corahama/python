#!/bin/python3

import math
import os
import random
import re
import sys


class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def queue(self, i):
        self.stack1.append(i)
    
    def dequeue(self):
        if len(self.stack2) == 0:
            for e in self.stack1[:0:-1]:
                self.stack2.append(e)
            self.stack1 = []
        else:
            self.stack2.pop()

    def print_front(self):
        if len(self.stack2) == 0:
            for e in self.stack1[::-1]:
                self.stack2.append(e)
            self.stack1 = []
        print(self.stack2[-1])


if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    queue = Queue()
    n = int(input().strip())

    for _ in range(n):
        i = list(map(int, input().rstrip().split()))
        if i[0] == 1:
            queue.queue(i[1])
        elif i[0] == 2:
            queue.dequeue()
        elif i[0] == 3:
            queue.print_front()
