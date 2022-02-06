"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

while True:
    user_numb = input('Введите целое число:')
    if user_numb.isdigit():
        user_numb = int(user_numb)
        break
    else:
        print('Вы не ввели целое положительное число')

"""
i = len(user_numb) - 1
max_numb = 0
while i >= 0:
    if int(user_numb[i]) > max_numb:
        max_numb = int(user_numb[i])
    i -= 1
print(max_numb)
"""
max_numb = 0
while user_numb > 0 and max_numb != 9:
    if (user_numb % 10) > max_numb:
        max_numb = user_numb % 10
    user_numb //= 10

print(max_numb)
