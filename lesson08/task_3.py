"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NumberCheck(Exception):
    def __init__(self, txt):
        self.txt = txt


res = []
while True:
    try:
        lst_el = input('Введите элемент списка (для выхода - нажмите "q"): ')
        if lst_el.lower() == 'q':
            break
        if not lst_el.isdigit():
            raise NumberCheck('Введенное значение не является числом')
        res.append(lst_el)
    except NumberCheck as err:
        print(err)
    finally:
        print(res)
