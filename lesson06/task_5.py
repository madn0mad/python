"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        return f'Это {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Это {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Это {self.title}'


xpen = Pen('ручка')
xpencil = Pencil('карандаш')
xhandle = Handle('маркер')
lst = [xpen, xpencil, xhandle]
for el in lst:
    print(el.draw())
