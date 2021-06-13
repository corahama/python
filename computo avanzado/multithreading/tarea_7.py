import threading
import numpy as np

def calculate_row(begin, end, step, A, B):
    global matrix_c
    for r in range(begin, end, step):
        row = []
        for j in range(B.shape[1]):
            v = 0
            for i in range(B.shape[0]):
                v += B[i][j]*A[r][i]
            row.append(v)
        matrix_c[r] = np.array(row)

if __name__ == "__main__":
    processors = 4
    M, L, N = [int(i) for i in input().split(',')]
    global matrix_c
    matrix_c = np.zeros(shape=(M, N), dtype=int)

    matrix_a = []
    for _ in range(M):
        matrix_a.append([int(i) for i in input().split(',')])
    matrix_a = np.array(matrix_a)

    matrix_b = []
    for _ in range(L):
        matrix_b.append([int(i) for i in input().split(',')])
    matrix_b = np.array(matrix_b)

    threads = []
    for i in range(processors):
        threads.append(threading.Thread(target=calculate_row, args=(i, matrix_a.shape[0], processors, matrix_a, matrix_b)))
        threads[-1].start()
    
    for i in range(processors):
        threads[i].join()
    
    print(f'{M},{N}')
    # print(matrix_c)
    for i in range(matrix_c.shape[0]):
        print(','.join(str(e) for e in matrix_c[i]))
