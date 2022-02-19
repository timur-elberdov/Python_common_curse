"""
 Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
"""


numbers = [i for i in range(20, 241) if (i % 20 == 0) or (i % 21 == 0)]
print(numbers)


def devisible(start, end, *deviders, all=False):
    """Функция возвращает список всех чисел, кратных deviders в интервале от start до end

    start - начало интервала
    end - конец интервала
    *dividers - числа, кратность которым возвратит функция
    all - параметр, указывающий, должна ли функция возвращать числа кратные всем devider, или любому из devider.
    all = True - функция возвратит только числа, кратные всем делителям

    """

    def all_deviders(num):
        divisibility = True
        for devider in deviders:
            if num % devider == 0:
                divisibility = True
            else:
                divisibility = False
                break
        return divisibility

    num_range = range(start, end+1)
    res = []

    if all:
        res = list(filter(all_deviders, num_range))
    else:
        for num in num_range:
            for devider in deviders:
                if num % devider == 0:
                    res.append(num)
    return res


new_numbers = devisible(20, 240, 2, 3, all=True)
print(new_numbers)
