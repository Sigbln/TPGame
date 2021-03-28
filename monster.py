class Monster:

    def __init__(self, name):
        species = {"Bugbear": [3, 1, 1], "Hobgoglin": [2, 3, 1], "Runner": [1, 2, 3]}
        self.__x = None
        self.__y = None
        self.__hp = species[name][0]
        self.__damage = species[name][1]
        self.__speed = species[name][2]

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

    def create(self):
        pass

    def move(self):
        pass

    def injure(self):
        pass

    def kill(self):
        pass

    def finish(self):
        pass
