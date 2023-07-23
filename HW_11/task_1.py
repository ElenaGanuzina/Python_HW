"""
Создайте класс Матрица. Добавьте методы для:
- вывода на печать,
- сравнения,
- сложения,
- *умножения матриц
"""


class Matrix:
    _rows = 0
    _columns = 0
    _matrix: list[list[int, float]] = None

    def __init__(self, matrix: list[list[int, float]]):
        self._rows = len(matrix)
        self._columns = len(matrix[0])
        self._matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self._matrix))

    def __repr__(self):
        return f'Matrix{self._matrix}'

    def __eq__(self, other) -> bool:
        return all(self._matrix[i][j] == other._matrix[i][j] for j in range(self._columns)
                   for i in range(self._rows))

    def __ne__(self, other) -> bool:
        return any(self._matrix[i][j] != other._matrix[i][j] for j in range(self._columns)
                   for i in range(self._rows))

    def __add__(self, other):
        if self._rows != other._rows or self._columns != other._columns:
            raise ValueError('Addition is not permitted for matrices of different dimensions.')
        else:
            return Matrix([[self._matrix[i][j] + other._matrix[i][j] for j in range(self._columns)]
                           for i in range(self._rows)])

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if self._columns != other._rows:
            raise ValueError('The columns number of one matrix is not equal '
                             'to the rows number of the other one.')
        else:
            new_matrix = [[0 for row in range(other._columns)] for col in range(self._rows)]
            for row in range(self._rows):
                for col in range(other._columns):
                    for item in range(self._columns):
                        new_matrix[row][col] += self._matrix[row][item] * other._matrix[item][col]
        return Matrix(new_matrix)

    def __rmul__(self, other):
        return self.__mul__(other)


def main():
    m = Matrix([[1, 2], [3, 4]])
    n = Matrix([[0, 9], [8, 7]])
    z = Matrix([[1, 2, 3], [4, 5, 6]])
    print(m)
    print(f'{m = }')
    print(n)
    print(f'{n = }')
    print(m == n)
    print(m != n)
    print(m + n)
    print(m * n)
    print(m + z)
    print(n * z)


if __name__ == '__main__':
    main()
