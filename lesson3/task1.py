"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(quotient,  divisor):
    try:
        return quotient / divisor
    except ZeroDivisionError:
        print('Делить на ноль нельзя')


a = map(float, (input('Введите числа, которые нужно разделить через пробел: ')).split())
print(division(*a))