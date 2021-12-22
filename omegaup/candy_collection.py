#!/usr/bin/python3

def max_interval(arr):
    _max = 0
    _curr = 0
    for i in arr:
        _curr = _curr + i
        _curr = max(_curr, 0)
        _max = max(_max, _curr)
    return _max


def _main() -> None:
    T = int(input())
    res = []
    for _ in range(T):
        N = int(input())
        arr = [int(a) for a in input().split()]
        if all(map(lambda x: x<0, arr)):
            res.append(max(arr))
        else:
            res.append(max_interval(arr))
    for i in range(T):
        print(f"Case #{i+1}: {res[i]}")


if __name__ == '__main__':
    _main()
