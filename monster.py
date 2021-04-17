import global_names


class Monster:

    def __init__(self, name):
        species = {"Bugbear": [3, 1, 1, 1], "Hobgoglin": [2, 3, 1, 1], "Runner": [1, 2, 3, 1]}
        self.__name = name
        self.__x = 0
        self.__y = 0
        self.point = 0
        self.__hp = species[name][0]
        self.__damage = species[name][1]
        self.__speed = species[name][2]
        self.__cost = species[name][3]

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
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        self.__point = point

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

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
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    def create(self):
        pass

    def move(self):
        pass

    def injure(self):
        pass

    def kill(self):
        global_names.MONSTERS.pop(global_names.MONSTERS.index(self))
        global_names.CASTLE.money += self.cost

    def finish(self):
        global_names.MONSTERS.pop(global_names.MONSTERS.index(self))
        global_names.CASTLE.hp -= self.damage
