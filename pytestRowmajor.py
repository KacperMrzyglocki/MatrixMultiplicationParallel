import numpy as np
import pytest


def matrix_multiply(A,B,C,N):
    if  A.shape[1] == B.shape[0]:
        for i in range(0,N,1): 
            for j in range(0,N,1):
                for k in range(0,N,1):
                  C[i,j]+= A[i,k]*B[k,j]
        return C
    else:
        return "Sorry, cannot multiply A and B."

@pytest.fixture
def setup_matrices():
    size = 256
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    C = np.zeros((A.shape[0],B.shape[1]),dtype = float)
    blockSize = 64
    return A, B, C, size

@pytest.mark.benchmark(min_rounds=5)
def test_matrix_multiply(benchmark, setup_matrices):
    A, B , C, N = setup_matrices

    result = benchmark(matrix_multiply, A, B, C, N)
    assert result is not None
