#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'photoAlbum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY index
#  2. INTEGER_ARRAY identity
#

def photoAlbum(index, identity):
    result = []

    for idx, itm in zip(index, identity):
        result.insert(idx, itm)

    return result

if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    index_count = int(input().strip())

    index = []

    for _ in range(index_count):
        index_item = int(input().strip())
        index.append(index_item)

    identity_count = int(input().strip())

    identity = []

    for _ in range(identity_count):
        identity_item = int(input().strip())
        identity.append(identity_item)

    result = photoAlbum(index, identity)

    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
