from abc import ABCMeta
from math import sqrt

import global_names
import monster
import random

class Cell(metaclass=ABCMeta):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        pass

    @x.setter
    def x(self, x):
        pass

    @property
    def y(self):
        pass

    @y.setter
    def y(self, y):
        pass


class Spawner(Cell):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Spawner._instance:
            Spawner._instance = super(Spawner, cls).__new__(cls)
        return Spawner._instance

    def __init__(self, x, y, power):
        self.__x = x
        self.__y = y
        self.__power = power

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

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power

    def spawn(self):
        for i in range(0, self.power):
            unit = monster.Monster(global_names.MONSTERS_NAMES[random.randint(0, 2)])
            global_names.MONSTERS.append(unit)


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

    def losehp(self):
        pass

    def destroy(self):
        pass


class Tower(Cell):
    def __init__(self, x, y, damage, speed, radius):
        self.__x = x
        self.__y = y
        self.__damage = damage
        self.__speed = speed
        self.__radius = radius

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

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def fire(self):
        for monster in global_names.MONSTERS:
            if sqrt((self.x * 40 + 20 - (monster.x + global_names.PATH[monster.point][0] * 40)) ** 2 +
                    (self.y * 40 + 20 - (monster.y + global_names.PATH[monster.point][1] * 40)) ** 2) <= self.radius:
                monster.hp -= self.damage
                if monster.hp <= 0:
                    monster.kill()
                break

    def create(self):
        pass

    def update(self):
        pass

    def destroy(self):
        pass
