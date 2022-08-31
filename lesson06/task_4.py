"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} двинулся с места'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction):
        return f'Автомобиль {self.name} повернул {direction}'

    def showspeed(self):
        return f'Текущая скорость автомобиля {self.name} - {self.speed}'


class TownCar(Car):
    def showspeed(self):
        if self.speed > 60:
            return f'Превышение скорости! Текущая скорость {self.speed}. Допустимая 60'
        else:
            return f'Текущая скорость автомобиля - {self.speed}'


class SportCar(Car):
    def showcarname(self):
        return f'Автомобиль - {self.name}'


class WorkCar(Car):
    def showspeed(self):
        if self.speed > 40:
            return f'Превышение скорости! Текущая скорость {self.speed}. Допустимая 40'
        else:
            return f'Текущая скорость автомобиля - {self.speed}'


class PoliceCar(Car):
    def showcarname(self):
        return f'Автомобиль - {self.name}'


lamb = SportCar(180, 'красный', 'Ламборджини', False)
print(f'{lamb.go()}\n{lamb.showspeed()}\n')
mercedes = PoliceCar(60, 'белый', 'патруль ДПС', True)
print(f'{mercedes.go()}\n{mercedes.turn("налево")}\n{mercedes.showspeed()}\n{mercedes.stop()}\n')
newcar = TownCar(40, 'зеленый', 'Renault Kaptur', False)
print(f'{newcar.go()}\n{newcar.turn("направо")}\n{newcar.showspeed()}\n{newcar.stop()}\n')
wcar = WorkCar(90, 'черный', 'hyundai solaris', False)
print(f'{wcar.go()}\n{wcar.showspeed()}')
