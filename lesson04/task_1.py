"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

salary_s, production_h, rate_h, premium = argv


def salary(production, rate, premium):
    try:
        print(f'Заработная плата составляет: {(int(production_h) * int(rate_h)) + int(premium)} рублей')
    except ValueError as e:
        print(e)


salary(production_h, rate_h, premium)
