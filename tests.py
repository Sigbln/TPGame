from abc import ABCMeta


class Cell(metaclass=ABCMeta):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


class Castle(Cell):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Castle._instance:
            Castle._instance = super(Castle, cls).__new__(cls)
        return Castle._instance

    def __init__(self, x, y, money, hp):
        super().__init__(x, y)
        self.__money = money
        self.__hp = hp

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp


def Testing_System():
    castle1 = Castle(0, 0, 0, 0)
    castle2 = Castle(1, 1, 1, 1)

    print("Проверка на существование объекта:", id(castle1) == id(castle2))
    print("Проверка на равенство объектов:", type(castle1) == type(castle2))
    print("Проверка характеристик первого объекта:", castle1.x, castle1.y, castle1.hp, castle1.money)
    print("Проверка характеристик второго объекта:", castle2.x, castle2.y, castle2.hp, castle2.money)


Testing_System()
