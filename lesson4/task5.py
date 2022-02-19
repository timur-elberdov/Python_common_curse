"""
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех
элементов списка. Подсказка: использовать функцию reduce().
"""

from functools import reduce

even_numbers = [num for num in range(1, 9) if not num & 1]
prod = reduce(lambda x, y: x*y, even_numbers)
print(prod)

