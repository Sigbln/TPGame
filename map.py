import pygame

import global_names


class Map:
    def __init__(self):
        self.__length = 27
        self.__width = 18
        self.__scheme = []

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length > 0 or isinstance(length, int):
            self.__length = length
        else:
            raise ValueError

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width > 0 and isinstance(width, int):
            self.__width = width
        else:
            raise ValueError

    @property
    def scheme(self):
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme):
        self.__scheme = scheme

    def create(self):
        pass

    def open(self):
        pass

    def print(self):
        """
        Выводит на экран карту
        """
        for temp_y in range(self.__width):
            for temp_x in range(self.__length):
                global_names.SCREEN.blit(
                    global_names.MAP.scheme[temp_y][temp_x],
                    (temp_x * 40, temp_y * 40))
