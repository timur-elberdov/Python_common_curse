"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('text_to_task3.txt', 'r', encoding='UTF-8') as modified_file:
    data = {item.split()[0]: int(item.split()[1]) for item in modified_file}

print('Сотрудники с заработной платой меньше 20 т.р.: '+ ', '.join([key for key in data if data[key] < 20000]))
print(f'Средняя зарплата: {sum(data.values()) / len(data.values())}')