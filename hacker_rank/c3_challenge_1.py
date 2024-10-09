#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'itemsSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY items as parameter.
#

def itemsSort(items):
    items.sort()
    items.sort(key=Counter(items).get)
    
    return items

if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    items_count = int(input().strip())

    items = []

    for _ in range(items_count):
        items_item = int(input().strip())
        items.append(items_item)

    result = itemsSort(items)

    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
