"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()
"""
my_list = []
while True:
    a = input('Введите значение нового элемента списка(введите пробел, чтобы закончить): ')
    if a != ' ':
        my_list.append(a)
    else:
        break

# Моё решение
for i in range(0, len(my_list), 2):
    if i == len(my_list) - 1:
        break
    my_list[i], my_list[i + 1] = my_list[i+1], my_list[i]
print(my_list)

# Решение на уроке
i = 0
while i < len(my_list) - 1:
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
print(my_list)



