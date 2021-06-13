from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if __name__ == "__main__":
    if rank == 0:
        datos = np.array([1,2,3,4])
    else:
        datos = None

    datos = comm.scatter(datos, root=0)

    print(datos)