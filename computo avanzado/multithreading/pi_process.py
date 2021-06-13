from multiprocessing import Pool
import numpy as np
import math

def process_bunch(start, iterations, step):
    prod = 1.0
    for i in range(start, iterations, step):
        prod *= (2*i)**2 / ((2*i-1)*(2*i+1))
    return prod

if __name__ == "__main__":
    iterations = 1000000000
    processors = 8

    pool = Pool(processors)
    results = [pool.apply_async(process_bunch, args=(i, iterations, processors,)) for i in range(1, processors+1)]
    pool.close()
    pool.join()

    pi_calculated = 2*np.prod([e.get() for e in results])

    print(f'pi python value:\t\t\t\t{math.pi}')
    print(f'pi calculated value with {iterations} iterations:\t{pi_calculated}')
