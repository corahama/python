from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def process_bunch(start, iterations, step):
    prod = 1.0
    for i in range(start, iterations, step):
        prod *= (2*i)**2 / ((2*i-1)*(2*i+1))
    return prod

if __name__ == "__main__":
    val_max = 10000000
    val = process_bunch(rank+1, val_max, size)
    valores = comm.gather(val, root=0)

    if rank == 0:
        pi_value = 2*np.prod(np.array(valores))
        print(pi_value)