"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


def string_word_count(text_file: str):
    with open(text_file, 'r', encoding='utf-8') as readed_file:
        file_lines = readed_file.readlines()
        print(f'В файле {text_file} {len(file_lines)} строки')
        for num, line in enumerate(file_lines):
            print(f'В строке №{num + 1} {len(line.split())} слова')

string_word_count('text_to_task2.txt')