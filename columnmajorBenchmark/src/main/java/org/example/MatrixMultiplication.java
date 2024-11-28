package org.example;

public class MatrixMultiplication {
	public void execute(double[][] A, double[][] B, double[][] C, int N) {
		for (int j = 0; j < N; j++) { // Loop over columns first
			for (int i = 0; i < N; i++) {
				C[i][j] = 0;
				for (int k = 0; k < N; k++) {
					C[i][j] += A[i][k] * B[k][j];  // Keep the correct multiplication logic
				}
			}
		}
	}
}
