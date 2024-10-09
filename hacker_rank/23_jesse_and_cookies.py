import heapq as hq
import sys
import re
import os


def cookies(k, A):
    res = 0

    while any(c < k for c in A) and len(A) > 1:
        last = hq.heappop(A)
        prelast = hq.heappop(A)
        
        new = last + 2*prelast
        
        hq.heappush(A, new)
        res += 1
        
    return res if all(c >= k for c in A) else -1


if __name__ == "__main__":
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    n, k = map(int, input().strip().split(' '))
    candies = list(map(int, input().strip().split(' ')))
    A = []
    for el in candies:
        hq.heappush(A, el)

    print(cookies(k, A))