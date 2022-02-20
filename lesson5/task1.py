"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
from os import path


def write_to_file(name):
    mode = 'a' if path.exists(name) else 'x'
    with open(f'{name}', f'{mode}', encoding='utf-8') as file_obj:
        while True:
            info = input('Введите данные (для выхода нажмите enter): ')
            if info == '':
                break
            else:
                file_obj.write(f'\n{info}')


write_to_file('text.txt')

with open('text.txt', encoding='utf-8') as file:
    print(file.read())
