# mpirun.mpich -np 4 python3 temp.py
from mpi4py import MPI
from random import randint

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(f'rank:{rank} size:{size}')
if rank != 0:
    data = randint(0,10)
    comm.send(data, dest=0, tag=1)
    print(f'{data} {rank}')

if rank == 0:
    info = []
    for i in range(1, size):
        info.append(comm.recv(source=i, tag=1))
    print(info)
