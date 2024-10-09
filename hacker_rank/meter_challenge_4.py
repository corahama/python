#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countDuplicate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def countDuplicate(numbers):
    numbers = [n for n in numbers if numbers.count(n) > 1]

    return len(set(numbers))

if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = countDuplicate(numbers)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
