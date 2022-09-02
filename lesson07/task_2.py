"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class AbcClothes(ABC):
    @abstractmethod
    def consumption_c(self):
        pass

    @abstractmethod
    def consumption_s(self):
        pass


class Clothes(AbcClothes):
    def __init__(self, clst, sze):
        self.clhs = clst
        self.size = sze

    def consumption_c(self):
        if self.clhs == 'c':
            return round(self.size / 6.5 + 0.5, 2)

    def consumption_s(self):
        if self.clhs == 's':
            return round(2 * self.size + 0.3, 2)


sum_c: int = 0
while True:
    clths = input(
        'Введите букву(лат.) для типа одежды (c - пальто,  s - костюм; q - для перехода к общему итогу): ').lower()
    if clths == 'c':
        size = int(input('Введите размер пальто: '))
        cls = Clothes(clths, size)
        print(f'Расход ткани на пальто = {cls.consumption_c()}')
        sum_c += cls.consumption_c()
    elif clths == 's':
        size = int(input('Введите рост: '))
        cls = Clothes(clths, size)
        print(f'Расход ткани на костюм = {cls.consumption_s()}')
        sum_c += cls.consumption_s()
    elif clths == 'q':
        break
    else:
        print('Неверное значение')
        exit(1)

print(f'Общий расход ткани = {sum_c}')
