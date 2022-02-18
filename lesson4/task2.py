"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randint, uniform
num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def only_bigger_num(x):
    return [item for index, item in enumerate(x) if index and item > x[index - 1]]


new_list = only_bigger_num(num_list)
# здесь условие index and item - чтобы убрать первый элемент. если индекс - будет тру во всех случаях, кроме нулевого
# индекса
print(new_list)

# Сгенерируем псевдослучайный список и проверим на нём


def random_range(quantity, start=0, end=10, int=True):
    if int:
        random_range = [randint(start, end) for i in range(quantity)]
    else:
        random_range = [uniform(start, end) for i in range(quantity)]
    return random_range

i = random_range(10, 2, 15)
print(i)
print(only_bigger_num(i))