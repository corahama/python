import threading
import math

factorial_bunch = []
def calculate_factorial(begin, end, step, n):
    result = 0
    for i in range(begin, end, step):
        result += int(n/5**i)
    factorial_bunch.append(result)    

if __name__ == "__main__":
    process = 4
    # process = int(input('Introduce la cantidad de hilos: '))
    # n = 10000
    n = int(input('Introduce el valor de n: '))

    kmax = int(math.log(n)/math.log(5))

    threads = []
    for i in range(1, process+1):
        threads.append(threading.Thread(target=calculate_factorial, args=(i, kmax+1, process, n)))
        threads[-1].start()

    for i in range(process):
        threads[i].join()
    
    print(sum(factorial_bunch))
