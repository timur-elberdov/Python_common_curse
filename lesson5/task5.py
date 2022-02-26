"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint


def rand_nums_to_file(quantity, start=0, end=10):
    random_range = [randint(start, end) for _ in range(quantity)]
    with open('text_to_task5.txt', 'w', encoding='UTF-8') as file:
        file.write(' '.join(map(str, random_range)))


rand_nums_to_file(10)

with open('text_to_task5.txt', 'r', encoding='UTF-8') as file:
    nums = file.read()

print(sum(map(int, nums.split())))
