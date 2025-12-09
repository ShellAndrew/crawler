from collections import defaultdict, deque
import matplotlib.pyplot as plt
import csv
import numpy as np

#100 cars of type P
#200 cars of type Q
column_vector = np.array([[100.0], [200.0]])
matrix_A = np.array([[0.8, 0.4], 
                    [0.2, 0.6]])

for i in range(40):
    new_col_vector = np.array([[0.0], [0.0]])
    for i in range(len(matrix_A)):
        for j in range(len(column_vector[0])):

            for k in range(len(column_vector)):
                new_col_vector[i][j] += matrix_A[i][k] * column_vector[k][j]
    column_vector = new_col_vector

print(column_vector)
