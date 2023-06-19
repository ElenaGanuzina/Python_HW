"""
Задача 1.

Напишите функцию для транспонирования матрицы.
"""


def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


matrix = [[33, 15, 2], [45, -6, 0]]
print(transpose_matrix(matrix))