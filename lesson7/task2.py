"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class ClothesInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fabric_consumption(self):
        pass


class Clothes(ClothesInterface):
    __assortment = []
    __common_fabric_consump = 0

    def __init__(self, type, article, model_name, size):
        self.type = type
        self.article = article
        self.model_name = model_name
        self.size = size

        __fabric_consump = {
            'Пальто': (self.size / 6.5 + 0.5),
            'Пиджак': (self.size * 2 + 0.3)
        }

        self.__fabric_consump = __fabric_consump[self.type]
        Clothes.__assortment.append(self.__dict__)
        Clothes.__common_fabric_consump += self.__fabric_consump


    @property
    def fabric_consumption(self):
        return self.__fabric_consump

    @property
    def common_fabric_consumption(self):
        return Clothes.__common_fabric_consump


a = Clothes('Пальто', '1', 'Зимнее', 10)
b = Clothes('Пальто', '1', 'Зимнее', 9)
c = Clothes('Пальто', '2', 'Осенне-весеннее', 10)
d = Clothes('Пальто', '2', 'Осенне-весеннее', 9)

i = Clothes('Пиджак', '3', 'Двупуговичный', 175)
f = Clothes('Пиджак', '3', 'Двупуговичный', 185)
j = Clothes('Пиджак', '4', 'Трёхпуговичный', 175)
h = Clothes('Пиджак', '4', 'Трёхпуговичный', 185)

print(a.fabric_consumption)
print(i.fabric_consumption)
print(a.fabric_consumption)

print(a.common_fabric_consumption)