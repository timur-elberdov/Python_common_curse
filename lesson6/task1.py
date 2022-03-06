"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""

from time import time
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__colour = 'red'
        self.__colours = cycle(('yellow', 'green', 'red'))
        self.__off = False

    def __switch_light(self, light_time):
        start = time()
        while True:
            if time() - start >= light_time:
                break
        self.__colour = next(self.__colours)

    def __colour_check(self, prev_colour):
        colour_check = ('red', 'yellow', 'green')
        return colour_check[(colour_check.index(self.__colour) - 1)] == prev_colour

    def running(self, red_time=7, yellow_time=2, green_time=7):
        for time in cycle([red_time, yellow_time, green_time]):
            prev_colour = self.__colour
            print(self.__colour)
            self.__switch_light(time)
            if not self.__colour_check(prev_colour):
                break


a = TrafficLight()
a.running()

