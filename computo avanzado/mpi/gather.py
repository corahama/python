from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if __name__ == "__main__":
    lista = rank
    valores = comm.gather(lista, root=0)

    if rank == 0:
        print(valores)