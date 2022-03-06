"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {'wage': None, 'bonus': None}

    _income = {'wage': None, 'bonus': None}

    def set_income(self, wage, bonus):
        self._income['wage'], self._income['bonus'] = wage, bonus

    def get_income(self):
        return self._income


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return f'{self._name} {self._surname}'

    def get_total_income(self):
        return sum(self._income.values())


a = Worker('Tim', 'Elb', 'ingener')

a.set_income(50000, 10000)

print(a.get_income())

b = Position('Tim', 'Elb', 'ingener')
b.set_income(200, 500)
print(b.get_income())
print(b.get_full_name())
print(b.get_total_income())
