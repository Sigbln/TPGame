import cell
import global_names


class Map:

    def __init__(self):
        self.__length = 27
        self.__width = 18
        self.__scheme = []
        self.WAVE_LONG = 20
        self.WAVE_NUMBER = 1

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

    def print(self, SCREEN, MAP):
        """
        Выводит на экран карту
        """
        for temp_y in range(self.__width):
            for temp_x in range(self.__length):
                SCREEN.blit(
                    MAP.scheme[temp_y][temp_x],
                    (temp_x * cell.Cell.SIZE, temp_y * cell.Cell.SIZE))

    def way_to_move(self, MAP, CASTLE, SPAWNER):
        """
        Создает карту пути по которому двигаются монстры
        """
        special_map = global_names.MAPS_COLLECTION[global_names.TEMP_ID]
        lab = []

        n = MAP.width
        m = MAP.length

        for i in range(n):
            line = []
            for k in range(len(special_map[i])):
                if special_map[i][k] == 1:
                    line.append(-1)
                elif special_map[i][k] == 2:
                    line.append(0)
                elif special_map[i][k] == 4:
                    CASTLE.x = i
                    CASTLE.y = k
                    line.append(0)
                elif special_map[i][k] == 3:
                    SPAWNER.x = i
                    SPAWNER.y = k
                    line.append(0)
                else:
                    line.append(special_map[i][k])
            lab.append(line)

        finalout = self.voln(SPAWNER.x, SPAWNER.y, 1, n, m, lab)
        if lab[CASTLE.x][CASTLE.y] > 0:
            path = self.way(SPAWNER.y, SPAWNER.x, CASTLE.y,
                            CASTLE.x,
                            finalout, MAP)
            path = path[::-1]
            global_names.PATH = path
        else:
            raise FileExistsError("Wrong way from spawner to castle")

    def voln(self, x, y, cur, n, m, lab):
        """
        Заполняет вспомогательный массив расстояниями от начальной клетки
        :param x: положение текущей клетки
        :param y: положение тукущей клетки
        :param cur: текущее значение клетки
        :param n: ширина поля
        :param m: длина поля
        :param lab: провежуточный массив растояний
        :return: заполненный расстояниями массив
        """
        lab[x][y] = cur
        if y + 1 < m:
            if lab[x][y + 1] == 0 or (lab[x][y + 1] != -1 and lab[x][y + 1] > cur + 1):
                self.voln(x, y + 1, cur + 1, n, m, lab)
        if x + 1 < n:
            if lab[x + 1][y] == 0 or (lab[x + 1][y] != -1 and lab[x + 1][y] > cur + 1):
                self.voln(x + 1, y, cur + 1, n, m, lab)
        if x - 1 >= 0:
            if lab[x - 1][y] == 0 or (lab[x - 1][y] != -1 and lab[x - 1][y] > cur + 1):
                self.voln(x - 1, y, cur + 1, n, m, lab)
        if y - 1 >= 0:
            if lab[x][y - 1] == 0 or (lab[x][y - 1] != -1 and lab[x][y - 1] > cur + 1):
                self.voln(x, y - 1, cur + 1, n, m, lab)
        return lab

    def way(self, x1, y1, x2, y2, lab, MAP):
        """
        Поиск пути в массиве растояний
        :param x1: начало пути
        :param y1: начало пути
        :param x2: конец пути
        :param y2: конец пути
        :param lab: массив расстояний
        :return: путь
        """
        n = MAP.width
        m = MAP.length

        path = [[x2, y2]]
        while (x1, y1) != (x2, y2):
            if x2 > 0 and lab[y2][x2 - 1] == lab[y2][x2] - 1:
                x2, y2 = x2 - 1, y2
            elif x2 < m - 1 and lab[y2][x2 + 1] == lab[y2][x2] - 1:
                x2, y2 = x2 + 1, y2
            elif y2 > 0 and lab[y2 - 1][x2] == lab[y2][x2] - 1:
                x2, y2 = x2, y2 - 1
            elif y2 < n - 1 and lab[y2 + 1][x2] == lab[y2][x2] - 1:
                x2, y2 = x2, y2 + 1
            path.append([x2, y2])
        return path
