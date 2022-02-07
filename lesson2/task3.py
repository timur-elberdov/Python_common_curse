"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

months_dict = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter'
}

months_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn',
               'autumn', 'winter']

while True:
    user_month = input('Введите номер месяца: ')
    if user_month.isdigit() and int(user_month) < 13:
        user_month = int(user_month)
        break
    else:
        print('Вы ввели не номер месяца')

print(months_dict[user_month])
print(months_list[user_month - 1])