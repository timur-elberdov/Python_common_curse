"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re

with open('text_to_task6.txt', 'r', encoding="UTF-8") as file:
    subjects = file.readlines()

subject_dict = {}

for line in subjects:
    subject = line[:line.find(':')]
    hours_blank = line[line.find(':') + 2:].split()
    hours = []
    for item in hours_blank:
        try:
            hours.append(int(item[:item.index('(')]))
        except ValueError:
            continue
    subject_dict[subject] = sum(hours)
print(subject_dict)


dict = {}
with open('text_to_task6.txt', 'r', encoding='UTF-8') as file:
    for string in file:
        hours = re.findall(r'\d+', rf'{string}')
        hours = sum([int(hour) for hour in hours])
        subject = re.match(r'\b\w+\b', rf'{string}').group()
        dict[subject] = hours

print(dict)
