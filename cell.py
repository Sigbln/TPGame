import random
from abc import ABCMeta
from math import sqrt

import global_names
import monster
#import graphic


class Cell(metaclass=ABCMeta):
    SIZE = 40
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


class Spawner(Cell):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Spawner._instance:
            Spawner._instance = super(Spawner, cls).__new__(cls)
        return Spawner._instance

    def __init__(self, x, y, power):
        super().__init__(x, y)
        self.__power = power
        self.monsters = monster.Monster

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power

    def spawn(self):
        """
        Создает монстра
        """
        for i in range(0, self.power, global_names.WAVE_NUMBER):
            unit = monster.Monster(self.monsters.names[random.randint(0, 2)])
            unit.hp *= global_names.WAVE_NUMBER
            unit.cost *= global_names.WAVE_NUMBER
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

    def destroy(self, PLAY, LEVELS, SPAWNER, CASTLE, MENU):
        """
        Окончание игры, в случае если hp опустиллось до 0
        """
        global_names.MONSTERS.clear()
        global_names.TOWERS.clear()
        global_names.PATH.clear()
        PLAY = False
        LEVELS = False
        MENU = True
        global_names.TIMER = -1
        SPAWNER = Spawner(0, 0, 10)
        CASTLE = Castle(0, 0, 100, 5)
        global_names.WAVE_NUMBER = 1

        return PLAY, LEVELS, SPAWNER, CASTLE, MENU


class Tower(Cell):
    TOWER_POWER = [2]
    TOWER_SPEED = [1]
    TOWER_RADIUS = [100]
    TOWER_CREATING_COST = 20
    TOWER_REMOVING_COST = 10

    def __init__(self, x, y, damage, speed, radius):
        super().__init__(x, y)
        self.__damage = damage
        self.__speed = speed
        self.__radius = radius

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

    def fire(self, CASTLE):
        """
        Наносит урон монстрам в радиусе атаки башни
        """
        for monsters in global_names.MONSTERS:
            if sqrt((self.x * self.SIZE + self.SIZE/2 - (monsters.x + global_names.PATH[monsters.point][0] * self.SIZE)) ** 2 +
                    (self.y * self.SIZE + self.SIZE/2 - (monsters.y + global_names.PATH[monsters.point][1] * self.SIZE)) ** 2) <= self.radius:
                monsters.hp -= self.damage
                monsters.injured = True
                if monsters.hp <= 0:
                    monsters.kill(CASTLE)
                break
