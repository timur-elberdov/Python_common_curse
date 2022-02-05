"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

user_numb = input('Введите целое число:')

result = int(user_numb) + int(user_numb*2) + int(user_numb*3)

print(result)

