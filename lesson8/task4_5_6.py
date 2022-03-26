"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
на уроках по ООП.
"""


class Warehouse:
    __count = 0

    def __init__(self, adress, area, capacity):
        self.__id = Warehouse.__count + 1
        Warehouse.__count += 1

        self.__adress = adress
        self.__area = area
        self.__capacity = capacity
        self.__load = 0

    @property
    def adress(self):
        return self.__adress

    @property
    def size(self):
        return self.__area

    @property
    def capacity(self):
        return self.__capacity

    @property
    def load(self):
        return self.__load

    @property
    def free_space(self):
        return self.__capacity - self.__load

    class Equipment:
        def __init__(self, article, type, model, price, size):
            self._article = article
            self._type = type
            self._model = model
            self._price = price
            self._size = size

    class Computer(Equipment):
        def __init__(self, article, type, model, price, size, ram, rom, proc):
            super().__init__(article, type, model, price, size)
            self._ram = ram
            self._rom = rom
            self._proc = proc

    class Printer(Equipment):
        def __init__(self, article, type, model, price, size, paper_size, is_colour):
            super().__init__(article, type, model, price, size)
            self._paper_size = paper_size
            self._is_colour = is_colour

