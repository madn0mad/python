"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

from datetime import date


class MyDate:
    def __init__(self, data):
        self.day_month_year = data

    @classmethod
    def get_dmy(cls, day_month_year):
        mday, mmonth, myear = [int(el) for el in day_month_year.split('.')]
        return f'{mday}.{mmonth}.{myear}'

    @staticmethod
    def valid(day_month_year):
        mday, mmonth, myear = [int(el) for el in day_month_year.split('.')]
        try:
            date(myear, mmonth, mday)
            return 'Все верно'
        except ValueError:
            return 'Ошибка в дате'


print(MyDate.valid('24.04.2020'))
print(MyDate.valid('32.08.2022'))
