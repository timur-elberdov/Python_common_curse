"""
2.	Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.2.	Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
while True:
    user_seconds = input('Введите количество секунд:')
    if user_seconds.isdigit():
        user_seconds = int(user_seconds)
        break
    else:
        print('Вы ввелчи не число')

hours = user_seconds // 3600
minutes = user_seconds % 3600 // 60
seconds = user_seconds % 3600 % 60

print(f'{hours:>02}:{minutes:>02}:{seconds:>02}')
# в f-строке :> указывает количество символов, которое должно быть в этой части. :>02 - должно быть минимум два символа,
# если их меньше, недостающее заменят нулём. (если не указывать ноль, будут просто пробелы)
