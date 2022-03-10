from functools import reduce

from multiprocessing import Pool, cpu_count
import numpy as np


def parallel_func(arr, i, proc, func):
    return [(i, func(arr[i])) for i in range(i, arr.shape[0], proc)]


class algorithm():
    def __init__(self):
        self.threshold = 2
    
    def run(self):
        arr = np.arange(10)

        proc = cpu_count()
        pool = Pool(proc)

        results = [pool.apply_async(parallel_func, args=(arr, i, proc, self.func)) for i in range(proc)]
        pool.close()
        pool.join()

        l_results = sorted(reduce(lambda total, l: total + l, [r.get() for r in results]))
        print(l_results)

    def func(self, a):
        return a < self.threshold

def main():
    algorithm().run()


if __name__ == '__main__':
    main()