"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_string = input('Введите что-нибудь: ')
user_list = user_string.split()
for num, word in enumerate(user_list):
    print(f'{num+1}. {word[:10]}')

