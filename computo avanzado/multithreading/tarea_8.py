from multiprocessing import Pool
import math

def calculate_factorial(begin, end, step, n):
    result = 0
    for i in range(begin, end, step):
        result += int(n/5**i)
    return result

if __name__ == "__main__":
    # process = 4
    process = int(input('Introduce la cantidad de hilos: '))
    # n = 10000
    n = int(input('Introduce el valor de n: '))

    kmax = int(math.log(n)/math.log(5))

    pool = Pool(process)
    results = [pool.apply_async(calculate_factorial, args=(i, kmax+1, process, n, )) for i in range(1, process+1)]
    pool.close()
    pool.join()

    print(sum([result.get() for result in results]))
