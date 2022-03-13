"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix
        self._rows = len(matrix)
        self._columns = len(matrix[0])

    def __str__(self):
        result = []
        for line in self.matrix:
            result.append(f'{" ".join(map(str, line))}\n')
        return ''.join(result)

    def __add__(self, other):
        if self._rows != other._rows or self._columns != other._columns:
            print('Невозможно выполнить сложение матриц разной размерности!')
        else:
            result_matrix = []
            for i, line in enumerate(self.matrix):
                result_matrix.append(list(map(lambda x,y: x + y, self.matrix[i], other.matrix[i])))
            return Matrix(result_matrix)


if __name__ == '__main__':
    m = Matrix([[1, 2, 3], [1, 2, 3]])
    a = Matrix([[1, 2, 3], [1, 2, 3]])
    b = a + m
    print(a)
    print(b)
