from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def anonymous_func(mensaje):
    return lista[rank]

if __name__ == "__main__":
    if rank == 0:
        lista = [1,2,3,4,5]
    else:
        lista = None

    lista = comm.bcast(lista, root=0)
    result = anonymous_func(lista)
    results = comm.gather(result, root=0)

    if rank == 0:
        print(results)
