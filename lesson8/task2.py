"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class ZeroExept(Exception):
    def __init__(self, txt='Делить на ноль нельзя'):
        self.txt = txt

    def __str__(self):
        return self.txt


def user_devision():
    a = int(input('Введите делитель'))
    b = int(input('Введите знаменатель'))
    if b == 0:
        raise ZeroExept()
    return a / b


try:
    user_devision()
except ZeroExept as e:
    print(e)
