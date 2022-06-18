from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def display():
	print("[0, 0, 0, 0, 0]")
	print("[0, 0, [0, 3], 0, 0]")
	print("[0, 0, [0, 3, 4], 0, 0]")
	print("[0, 0, [0, 4], 0, 0]")
	print("[0, 0, 0, 0, 0]")

if rank == 0:
	display()