from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def display():
	print("Coordenador 1 falhou. Eu, 0 convoco eleições.")
	print("Eu, 0 perdi as eleições. 3 irá realizar novas eleições.")
	print("Eu, 3 sou o novo coordenador.")

if rank == 0:
	display()