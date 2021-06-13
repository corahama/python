from mpi4py import MPI
import numpy as np
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def process_bunch(start, iterations, step):
    prod = 1.0
    for i in range(start, iterations, step):
        prod *= (2*i)**2 / ((2*i-1)*(2*i+1))
    return prod

if __name__ == "__main__":
    iterations = 1000000

    if rank != 0:
        comm.send(process_bunch(rank, iterations, size-1), dest=0, tag=1)

    if rank == 0:
        info = [comm.recv(source=i, tag=1) for i in range(1,size)]

        pi_calculated = 2*np.prod(info)

        print(f'pi python value:\t\t\t\t{math.pi}')
        print(f'pi calculated value with {iterations} iterations:\t{pi_calculated}')
