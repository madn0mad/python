"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    def __init__(self, matrx):
        self.matrx = matrx

    def __str__(self):
        for i in self.matrx:
            for j in i:
                print(f"{j:2}", end=' ')
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.matrx)):
            for j in range(len(other.matrx[i])):
                self.matrx[i][j] = self.matrx[i][j] + other.matrx[i][j]
        return Matrix.__str__(self)


first_m = Matrix([[3, 1, 0], [5, 14, -2], [4, 8, 12]])
second_m = Matrix([[8, 0, 1, ], [6, 7, 3], [-5, 2, 3]])
print('Первая матрица:')
print(first_m)
print('Вторая матрица:')
print(second_m)
print('Сумма матриц:')
print(first_m + second_m)
