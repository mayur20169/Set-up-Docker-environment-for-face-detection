import numpy as np
import threading


matrix_size = 1000

matrix_X = np.random.rand(matrix_size, matrix_size)
print(matrix_X, matrix_X.shape)
matrix_Y = np.random.rand(matrix_size, matrix_size)
print(matrix_Y, matrix_Y.shape)

matrix_Z = np.zeros((matrix_size, matrix_size))

def multiply_row(x, y, result, i, j, row):
    for k in range(row):
        for l in range(row):
            result[i+k][j+l] = sum(x[i+k][m] * y[m][j+l] for m in range(row))

def parallel_matrix_multiplication(x, y, result, row):
    num_threads = row
    threads = []

    for i in range(0, len(x), row):
        for j in range(0, len(y[0]), row):
            thread = threading.Thread(target=multiply_row, args=(x, y, result, i, j, row))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

row = 10

parallel_matrix_multiplication(matrix_X, matrix_Y, matrix_Z, row)

print(matrix_Z, matrix_Z.shape)                                            