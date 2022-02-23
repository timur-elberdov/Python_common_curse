"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from timeit import repeat, timeit
from os import remove


eng_rus_dict = {
    'one': 'Один',
    'two': 'Два',
    'three': 'Три',
    'four': 'Четыре',
    'five': 'Пять',
    'six': 'Шесть',
    'seven': 'Семь',
    'eight': 'Восемь',
    'nine': 'Девять',
    'ten': 'Десять',
}


def eng_num_to_rus1(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        old_list = file.read().lower()

    for key in eng_rus_dict:
        if key in old_list:
            old_list = old_list.replace(key, eng_rus_dict[key])

    with open('text_to_task4_rus.txt', 'w', encoding='utf-8') as file:
        file.write(old_list)
    remove('text_to_task4_rus.txt')
    del old_list


def eng_num_to_rus2(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        old_list = list(map(lambda x: x.lower().split(), file.readlines()))

    for num, line in enumerate(old_list):
        if line[0] in eng_rus_dict.keys():
            old_list[num][0] = eng_rus_dict[line[0]]
    with open('text_to_task4_rus.txt', 'w', encoding='utf-8') as file:
        for line in old_list:
            file.write(' '.join(line) + '\n')
    remove('text_to_task4_rus.txt')
    del old_list


text_to_task4_eng = 'text_to_task4_eng.txt'
setup_1 = "from __main__ import eng_num_to_rus1, text_to_task4_eng"
print(sum(repeat('eng_num_to_rus1(text_to_task4_eng)', setup_1, repeat=5, number=100)) / 5)
print(timeit('eng_num_to_rus1(text_to_task4_eng)', setup_1, number=100))

setup_2 = "from __main__ import eng_num_to_rus2, text_to_task4_eng"
print(sum(repeat('eng_num_to_rus2(text_to_task4_eng)', setup_2, repeat=5, number=100)) / 5)
print(timeit('eng_num_to_rus2(text_to_task4_eng)', setup_2, number=100))



