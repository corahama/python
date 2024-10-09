#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'featuredProduct' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY products as parameter.
#

def featuredProduct(products):
    products.sort()
    products.sort(key=Counter(products).get)
    
    return products[-1]

if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    products_count = int(input().strip())

    products = []

    for _ in range(products_count):
        products_item = input()
        products.append(products_item)

    result = featuredProduct(products)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
