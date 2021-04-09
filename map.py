from tools import SingletonMeta


class Map(metaclass=SingletonMeta):
    maxLength = 100
    maxWidth = 100

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
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
        if len(self.__length) != self.__scheme:
            self.__scheme = scheme
        else:
            raise ValueError

    def create(self):
        print("Введите количество клеток в длину:")
        length = int(input())
        self.__length = length

        print("Введите количество клеток в ширину:")
        width = int(input())
        self.__width = width

        print(
            "Составьте карту по следующему принципу: карта -- это массив из символов, где . - обычная клетка,"
            " # - спавнер, % - замок, * - башня, стрелочки(_) - путь")
        for i in range(self.__width):
            self.__scheme.append(input())

        menu_output =
        """
        Хотите ли вы сохранить карту?
        1. Да,
        2. Нет.
        """
        print(menu_output)
        option = int(input())
        while not isinstance(option, int) or option < 1 or option > 2:
            print("Неверный ввод.")
            print("Попробуйте ещё раз.")
            option = int(input())

        if option == 1:
            print("Введите название файла:")
            name = input()
            file = open(name + ".txt", 'w')
            for i in self.__scheme:
                file.write(i + '\n')
            file.close()

    def open(self):
        print("Введите название файла:")
        name = input()
        file = open(name + ".txt", 'r')
        for line in file:
            self.__scheme.append(line)

    def print(self):
        for row in self.__scheme:
            print(row)
