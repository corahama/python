from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if __name__ == "__main__":
    if rank == 0:
        print("Hola desde el proceso maestro")
        valores = [1,2,3,4]
        valores1 = [4,3,2,1]
        comm.send(valores, dest=1, tag=2)
        if size > 2:
            comm.send(valores1, dest=3, tag=3)
    elif rank == 1:
        print(f"Hola mundo desde el proceso {rank}")
        valores = comm.recv(source=0, tag=2)
        print(valores)
    elif rank == 3:
        print(f"Hola mundo desde el proceso {rank}")
        valores = comm.recv(source=0, tag=3)
        print(valores)
