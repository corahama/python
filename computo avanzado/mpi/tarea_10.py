from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def calculate_row(begin, end, step, A, B):
    results = []
    for r in range(begin, end, step):
        row = []
        for j in range(B.shape[1]):
            v = 0
            for i in range(B.shape[0]):
                v += B[i][j]*A[r][i]
            row.append(v)
        results.append((r, row))
    return results


if __name__ == "__main__":
    if rank == 0:
        M, L, N = [int(i) for i in input().split(',')]
        matrix_c = np.zeros(shape=(M, N), dtype=int)
        
        matrix_a = []
        for _ in range(M):
            matrix_a.append([int(i) for i in input().split(',')])
        matrix_a = np.array(matrix_a)

        matrix_b = []
        for _ in range(L):
            matrix_b.append([int(i) for i in input().split(',')])
        matrix_b = np.array(matrix_b)

        matrices = [matrix_a, matrix_b]
    else:
        matrices = None

    matrices = comm.bcast(matrices, root=0)
    result = calculate_row(rank, matrices[0].shape[0], size, matrices[0], matrices[1])
    results = comm.gather(result, root=0)

    if rank == 0:
        while [] in results:
            results.remove([])

        results = sorted([e for result in results for e in result if result], key=lambda x: x[0])

        index = 0
        for row in results:
            matrix_c[index] = row[1]
            index += 1

        print(f'{M},{N}')
        # print(matrix_c)
        for i in range(matrix_c.shape[0]):
            print(','.join(str(e) for e in matrix_c[i]))