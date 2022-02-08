"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_info(f_name, l_name, birth_y, city, email, number):
    print(f'{f_name} {l_name}, родился в {birth_y}г., проживает в городе {city}, email: {email}, телефон: {number}')


user1 = {
    'f_name': 'Timur',
    'l_name': 'Elberdov',
    'city': 'Moscow',
    'email': 't.e@mail.ru',
    'number': '+7 955 666 789 85',
    'birth_y': '1996'
}

user_info(**user1)

