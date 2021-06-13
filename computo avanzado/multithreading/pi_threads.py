import threading
import numpy as np
import math

data = []
def process_bunch(start, iterations, step):
    data.append(np.prod(np.array(([((2*i)**2) / ((2*i-1)*(2*i+1)) for i in range(start, iterations+1, step)]))))

if __name__ == "__main__":
    iterations = 10000000
    processors = 4

    threads = []
    for i in range(1, processors+1):
        threads.append(threading.Thread(target=process_bunch, args=(i, iterations, processors, )))
        threads[-1].start()

    for i in range(processors):
        threads[i].join()

    pi_calculated = 2*np.prod(data)

    print(f'pi python value:\t\t\t\t{math.pi}')
    print(f'pi calculated value with {iterations} iterations:\t{pi_calculated}')
