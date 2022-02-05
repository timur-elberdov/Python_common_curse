"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

user_numb = input('Введите целое число:')
i = len(user_numb) - 1
max_numb = 0
while i >= 0:
    if int(user_numb[i]) > max_numb:
        max_numb = int(user_numb[i])
    i -= 1

print(max_numb)