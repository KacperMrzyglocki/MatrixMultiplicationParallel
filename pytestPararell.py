import numpy as np
import pytest
import threading
from threading import Thread
import psutil

def process(A,B,C,N,startRow,endRow):
    for i in range(startRow,endRow,1):
        for j in range(0,N,1):
            for k in range(0,N,1):
                C[i,j]+=A[i,j]*B[k,j]

def matrix_multiply(A,B,C,N,numThreads):
    tasks=[]
    rowsPerThread = int(N/numThreads)
    remainingRows = int(N%numThreads)

    startRow=0
    for i in range(0,numThreads,1):
        endRow = startRow+rowsPerThread
        if i<remainingRows:
            endRow+=1
        tasks.append(Thread(target=process, args=(A,B,C,N,startRow,endRow)))
        tasks[i].start()
        startRow = endRow
    for i in range(0,numThreads,1):
        tasks[i].join()
    
@pytest.fixture
def setup_matrices():
    size = 256
    numThreads=12
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    C = np.zeros((size,size),dtype = float)
    return A,B,C,size,numThreads

@pytest.mark.benchmark(min_rounds=5)
def test_matrix_multiply(benchmark, setup_matrices):
    A, B, C, N, numThreads = setup_matrices

    result = benchmark(matrix_multiply, A, B, C, N, numThreads)
    assert result is not None

size = 128
numThreads=12
A = np.random.rand(size, size)
B = np.random.rand(size, size)
C = np.zeros((size,size),dtype = float)
matrix_multiply(A,B,C,size,numThreads)
print(psutil.cpu_percent())
print(psutil.virtual_memory().percent)
