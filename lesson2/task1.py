"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

my_list = [0, 'a', 5.585, complex(1, 2), (5, 8, 7), {'a', 58}, frozenset({'a', 58}), {1: '1'}, b'text',
           bytearray(b"some text"), True, None, NameError, BaseException]

for i in my_list:
    print(type(i))

