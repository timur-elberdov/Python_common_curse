"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date: str):
        self.day, self.month, self.year = \
            date.split('-')[0].zfill(2), date.split('-')[1].zfill(2), date.split('-')[2]
        self.date = (self.day, self.month, self.year)

    @classmethod
    def date_to_num(cls, date: str):
        return sum(map(int, date.split('-')))

    @staticmethod
    def date_validation(date: str):
        day, month, year = int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2])
        if not 0 < day < 31:
            raise ValueError('Некорректно введён день!')
        if not 0 < month < 12:
            raise ValueError('Некорректно введён месяц!')
        if not -1 < year:
            raise ValueError('Некорректно введён год')
        print('Дата корректна')
a = Date('1-1-2012')

b = Date.date_to_num("01-01-2012")
print(b)
Date.date_validation('5-11-2010')
Date.date_validation('01-15-2110')
print(a.date)