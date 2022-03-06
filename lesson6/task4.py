"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, name, colour, is_police=False):
        self.name = name
        self.colour = colour
        self._is_police = is_police
        self._speed = None

    def go(self, speed):
        self._speed = speed
        print(f'Машина поехала со скоростью {self._speed}')

    def stop(self):
        self._speed = 0
        print('Машина остановилась')

    def set_speed(self, speed):
        if self._speed:
            self._speed = speed
            print(f'Машина изменила скорость на {self._speed}')
        else:
            print('Машина не может изменить скорость, она не едет.')

    def show_speed(self):
        print(f'Скорость машины: {self._speed}')

    @staticmethod
    def turn(direction):
        dirr = {'r': 'направа', 'l': 'налево'}
        print(f'Машина повернула {dirr[direction]}')


class TownCar(Car):
    def __init__(self, name, colour):
        super().__init__(name, colour)
        self._is_police = False

    def show_speed(self):
        if self._speed > 60:
            print(f'Превышено ограничение скорости! Скорость машины: {self._speed} - на {self._speed - 40} '
                  'больше разрешённой')
        else:
            print(f'Скорость машины: {self._speed}')


class WorkCar(Car):
    def __init__(self, name, colour):
        super().__init__(name, colour)
        self._is_police = False

    def show_speed(self):
        if self._speed > 40:
            print(f'Превышено ограничение скорости! Скорость машины: {self._speed} - на {self._speed - 40} '
                  'больше разрешённой')
        else:
            print(f'Скорость машины: {self._speed}')


class PoliceCar(Car):
    def __init__(self, name, colour):
        super().__init__(name, colour)
        self._is_police = True


car = Car('BMW', 'Green')

car.go(50)
car.turn('r')
car.stop()

town_car = TownCar('Reno', 'Black')
town_car.go(80)
town_car.show_speed()
