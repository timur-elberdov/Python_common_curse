"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


def my_func1(x, y):
    return x**y


print(my_func1(10, 2))


def my_func2(x, y):
    res = 1
    for i in range(0, abs(y)):
        res *= x
    return res if y >= 0 else 1 / res


print(my_func2(1, -2))
