"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, cn1, cn2):
        self.rl = cn1
        self.im = cn2

    def __add__(self, other):
        _real_res = self.rl + other.rl
        _imag_res = self.im + other.im
        if _imag_res < 0:
            return f'{_real_res} - {abs(_imag_res)}j'
        return f'{_real_res} + {_imag_res}j'

    def __mul__(self, other):
        _real_res = self.rl * other.rl - self.im * other.im
        _imag_res = self.rl * other.im + self.im * other.rl
        if _imag_res < 0:
            return f'{_real_res} - {abs(_imag_res)}j'
        return f'{_real_res} + {_imag_res}j'


a = ComplexNumber(3, 1)
b = ComplexNumber(2, -3)

print(f'Сумма заданных комплексных чисел равна ({a + b})')
print(f'Произведение заданных комплексных чисел равно ({a * b})')
