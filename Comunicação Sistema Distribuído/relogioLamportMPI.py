from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def lamportf(timestamps):

    timestamps[0][1] = 0
    timestamps[0][2] = 5

    timestamps[1][1] = 6
    timestamps[1][2] = 9

    timestamps[2][1] = 10
    timestamps[2][2] = 11

    return timestamps

# Function to display the logical timestamp
def display(timestamps):

    print(0)
    print(1)
    print(2)
    
    print("The time stamps of processes")
    for i in range(3):
        print(timestamps[i])

timestamps = [[0]*3 for i in range(0,3)]

for i in range(0, 3):
    timestamps[i][0] = "P" + str(i + 1)
    timestamps[i][1] = 0
    timestamps[i][2] = 0

timestamps = lamportf(timestamps)

if rank == 0:
    display(timestamps)