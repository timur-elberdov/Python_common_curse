"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
import os


def write_to_file(f_name, f_path=os.path.dirname(__file__)):
    f_path_name = os.path.join(f_path, f_name)
    mode = 'a' if os.path.exists(f_path_name) else 'x'
    with open(rf'{f_path_name}', f'{mode}', encoding='utf-8') as file_obj:
        while True:
            user_data = input('Введите данные (для выхода нажмите enter): ')
            if user_data == '':
                break
            else:
                file_obj.write(f'\n{user_data}')


write_to_file('text.txt')

with open('text.txt', encoding='utf-8') as file:
    print(file.read())
