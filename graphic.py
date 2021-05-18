import pygame

import cell
import global_names
import map
import saver

pygame.init()


class Graphic:

    def __init__(self):
        self.saver = saver.saver()
        self.map = map.Map()
        self.towers = cell.Tower
        self.SPAWNER = cell.Spawner(0, 0, 10)
        self.CASTLE = cell.Castle(0, 0, 100, 5)

        self.menu_button_level = pygame.image.load("images/menunutton1.jpg")
        self.menu_button_editor = pygame.image.load("images/menunutton2.jpg")
        self.play_button = pygame.image.load("images/play_button.jpg")
        self.delete_button = pygame.image.load("images/delete_button.jpg")
        self.left_arrow = pygame.image.load("images/right_arrow.jpg")
        self.right_arrow = pygame.image.load("images/left_arrow.jpg")
        self.temp_bg = pygame.image.load("images/temp_bg.jpg")
        self.grass = pygame.image.load("images/grass.jpg")
        self.castle = pygame.image.load("images/castle.jpg")
        self.spawner = pygame.image.load("images/spawner.jpg")
        self.road = pygame.image.load("images/road.jpg")
        self.cell_menu = pygame.image.load("images/cell_menu.jpg")
        self.save_message = pygame.image.load("images/save_message.jpg")
        self.monster = pygame.image.load("images/monster.png")
        self.tower = pygame.image.load("images/tower.jpg")
        self.game_hud = pygame.image.load("images/game_hud.png")
        self.damaged_monster = pygame.image.load("images/damaged_monster.png")
        self.DICTIONARY_TO = {self.grass: 1, self.road: 2, self.spawner: 3,
                              self.castle: 4}
        self.DICTIONARY_FROM = {1: self.grass, 2: self.road, 3: self.spawner,
                                4: self.castle}

        self.FONT_SIZE = 40
        self.HP_POINT = (950, 607)
        self.COIN_POINT = (1010, 650)
        self.WAVE_POINT = (1000, 690)
        self.SCREENSIZE = (1080, 720)
        self.FPS = 30
        self.ORDINARY_START_POINT = (0, 0)
        self.SAVE_START_POINT = (415, 320)
        self.CELL_MENU_POINTS = (
            (455, 335), (458, 341, 498, 381), (501, 341, 541, 381),
            (544, 341, 584, 381),
            (587, 341, 627, 381))
        self.LEVELS_ARROWS_POINTS = (
            (0, 360), (1040, 360), (0, 360, 40, 400), (1040, 360, 1080, 400))
        self.LEVELS_PLAY_POINTS = ((300, 605), (300, 605, 500, 680))
        self.LEVELS_DELETE_POINTS = ((580, 605), (580, 605, 780, 680))
        self.MENU_BUTTON_1_POINT = ((440, 300), (440, 300, 640, 375))
        self.MENU_BUTTON_2_POINT = ((440, 405), (440, 405, 640, 480))
        self.GAME_HUD_START_POINT = (880, 600)
        self.WHITE = (255, 255, 255)
        self.EVENT = None
        self.CLOCK = None
        self.SCREEN = None
        self.font = pygame.font.Font(None, self.FONT_SIZE)
        self.hp = None
        self.coin = None
        self.wave = None
        self.RUN = True
        self.MENU = True
        self.EDITOR = False
        self.LEVELS = False
        self.CELL_MENU = False
        self.PLAY = False
        self.SAVE = False

    def update(self):
        """
        Обновляет значение hp, coin, wave
        """
        self.hp = self.font.render(str(self.CASTLE.hp), True, self.WHITE)
        self.coin = self.font.render(str(self.CASTLE.money), True,
                                     self.WHITE)
        self.wave = self.font.render(str(global_names.WAVE_NUMBER), True, self.WHITE)

    def create_map(self):

        """
        Создает карту, заполненную картинками травы если действие происходит в редакторе и
        если действие происходит в меню выбора уровня создает карту которая находится в массиве
        карт под номером TEMP_ID
        """

        for i in range(self.map.width):
            temp = []
            for j in range(self.map.length):
                temp.append(self.grass)
            self.map.scheme.append(temp)
        if self.LEVELS:
            self.map.scheme = self.saver.convert(self.DICTIONARY_FROM, self.map)

    def set_fps(self, fps):
        self.CLOCK = pygame.time.Clock()
        self.CLOCK.tick(fps)

    @staticmethod
    def get_mouse_for_button(pos):
        """
        Проверяет попало ли нажатие мышки на местоположение кнопки или же нет
        :param pos: местоположение копки
        :return: было ли нажатие мышкой на кнопку
        """
        mouse = pygame.mouse.get_pos()
        if pos[0] <= mouse[0] <= pos[2] and pos[1] <= mouse[1] <= pos[3]:
            return True
        return False

    def get_mouse_for_cell(self):
        """
        По нажатию мышки получает на какую клетку было совершено нажатие
        """
        global_names.TEMP_CELL = list(pygame.mouse.get_pos())
        global_names.TEMP_CELL[0] = global_names.TEMP_CELL[
                                        0] // cell.Cell.SIZE
        global_names.TEMP_CELL[1] = global_names.TEMP_CELL[
                                        1] // cell.Cell.SIZE

    def create_window(self):
        self.SCREEN = pygame.display.set_mode(
            self.SCREENSIZE)
        pygame.display.set_caption("TD v1.0")

    def key_check_menu(self):
        """
        Проверяет нажатие кнопок в меню и реагирует на них
        """
        for self.EVENT in pygame.event.get():
            if self.EVENT.type == pygame.QUIT:
                self.RUN = False
            if self.EVENT.type == pygame.MOUSEBUTTONDOWN:
                if self.get_mouse_for_button(
                        self.MENU_BUTTON_1_POINT[1]):
                    self.LEVELS = True
                    self.MENU = False
                    self.create_map()
                if self.get_mouse_for_button(
                        self.MENU_BUTTON_2_POINT[1]):
                    self.EDITOR = True
                    self.MENU = False
                    self.create_map()

    def draw_window_menu(self):
        """
        Отрисовывает окно меню
        """
        self.SCREEN.blit(self.temp_bg,
                         self.ORDINARY_START_POINT)
        self.SCREEN.blit(self.menu_button_level,
                         self.MENU_BUTTON_1_POINT[0])
        self.SCREEN.blit(self.menu_button_editor,
                         self.MENU_BUTTON_2_POINT[0])
        pygame.display.update()

    def key_check_editor(self):
        """
        Проверяет нажатие кнопок в редакторе и реагирует на них
        """
        for self.EVENT in pygame.event.get():
            if self.EVENT.type == pygame.QUIT:
                self.RUN = False
            elif self.EVENT.type == pygame.MOUSEBUTTONDOWN:
                # менюшка с выбором клеток для карты
                if self.CELL_MENU:
                    # земля
                    if self.get_mouse_for_button(
                            self.CELL_MENU_POINTS[1]):
                        self.map.scheme[global_names.TEMP_CELL[1]][
                            global_names.TEMP_CELL[0]] = self.grass
                    # дорога
                    elif self.get_mouse_for_button(
                            self.CELL_MENU_POINTS[2]):
                        self.map.scheme[global_names.TEMP_CELL[1]][
                            global_names.TEMP_CELL[0]] = self.road
                    elif self.get_mouse_for_button(
                            self.CELL_MENU_POINTS[3]):
                        self.map.scheme[global_names.TEMP_CELL[1]][
                            global_names.TEMP_CELL[0]] = self.spawner
                    elif self.get_mouse_for_button(
                            self.CELL_MENU_POINTS[4]):
                        self.map.scheme[global_names.TEMP_CELL[1]][
                            global_names.TEMP_CELL[0]] = self.castle
                    self.CELL_MENU = False
                else:
                    self.get_mouse_for_cell()
                    self.CELL_MENU = True
            # save_after_editor map
            if self.EVENT.type == pygame.KEYDOWN:
                if self.EVENT.key == pygame.K_s:
                    self.saver.save_after_editor(self.DICTIONARY_TO, self.map)
                    self.EDITOR = False
                    self.MENU = True

    def draw_window_editor(self):
        """
        Отрисовывает окно редактора
        """
        self.map.print(self.SCREEN, self.map)
        if self.CELL_MENU:
            self.SCREEN.blit(self.cell_menu,
                             self.CELL_MENU_POINTS[0])
        pygame.display.update()

    def key_check_levels(self):
        """
        Проверяет нажатие кнопок в меню выбора уровня и в самой игре, реагирует на них
        """
        for self.EVENT in pygame.event.get():
            if self.EVENT.type == pygame.QUIT:
                self.RUN = False
            if self.EVENT.type == pygame.MOUSEBUTTONDOWN:
                if self.PLAY:
                    self.get_mouse_for_cell()
                    if self.map.scheme[global_names.TEMP_CELL[1]][
                        global_names.TEMP_CELL[0]] == self.grass:
                        # ставит башню там где был произведен клик мышкой
                        if self.CASTLE.money >= self.towers.TOWER_CREATING_COST:
                            self.map.scheme[global_names.TEMP_CELL[1]][
                                global_names.TEMP_CELL[0]] = self.tower
                            global_names.TOWERS.append(
                                cell.Tower(global_names.TEMP_CELL[0],
                                           global_names.TEMP_CELL[1],
                                           self.towers.TOWER_POWER[0],
                                           self.towers.TOWER_SPEED[0],
                                           self.towers.TOWER_RADIUS[0]))
                            self.CASTLE.money -= self.towers.TOWER_CREATING_COST
                    elif self.map.scheme[global_names.TEMP_CELL[1]][
                        global_names.TEMP_CELL[0]] == self.tower:
                        # убирает башню если по ней был произведен клик мышкой
                        self.map.scheme[global_names.TEMP_CELL[1]][
                            global_names.TEMP_CELL[0]] = self.grass
                        for tower in global_names.TOWERS:
                            if tower.x == global_names.TEMP_CELL[
                                0] and tower.y == \
                                    global_names.TEMP_CELL[1]:
                                global_names.TOWERS.remove(tower)
                                self.CASTLE.money += self.towers.TOWER_REMOVING_COST
                else:
                    # стрелка влево
                    if self.get_mouse_for_button(
                            self.LEVELS_ARROWS_POINTS[2]):
                        print(len(global_names.MAPS_COLLECTION))
                        if global_names.TEMP_ID in range(1,
                                                         len(global_names.MAPS_COLLECTION)):
                            global_names.TEMP_ID -= 1
                            self.map.scheme = self.saver.convert(
                                self.DICTIONARY_FROM, self.map)
                    # стрелка вправо
                    elif self.get_mouse_for_button(
                            self.LEVELS_ARROWS_POINTS[3]):
                        if global_names.TEMP_ID in range(
                                len(global_names.MAPS_COLLECTION) - 1):
                            global_names.TEMP_ID += 1
                            self.map.scheme = self.saver.convert(
                                self.DICTIONARY_FROM, self.map)
                            print("p")
                    # кнопка начала игры
                    elif self.get_mouse_for_button(
                            self.LEVELS_PLAY_POINTS[1]):
                        self.PLAY = True
                        self.map.way_to_move(self.map, self.CASTLE, self.SPAWNER)
                    # кнопка удаления карты
                    elif self.get_mouse_for_button(
                            self.LEVELS_DELETE_POINTS[1]):
                        global_names.MAPS_COLLECTION.pop(global_names.TEMP_ID)
                        global_names.TEMP_ID = global_names.EMPTY
                        self.map.scheme = self.saver.convert(
                            self.DICTIONARY_FROM, self.map)

    def draw_window_levels(self):
        """
        Отрисоввывает окно выбора уровня или окно самой игры
        """
        self.map.print(self.SCREEN, self.map)
        if self.PLAY:
            for unit in global_names.MONSTERS:
                if not unit.injured:
                    self.SCREEN.blit(self.monster, (
                        unit.y + global_names.PATH[unit.point][0] * cell.Cell.SIZE,
                        unit.x + global_names.PATH[unit.point][1] * cell.Cell.SIZE))
                else:
                    self.SCREEN.blit(self.damaged_monster, (
                        unit.y + global_names.PATH[unit.point][0] * cell.Cell.SIZE,
                        unit.x + global_names.PATH[unit.point][1] * cell.Cell.SIZE))

            self.SCREEN.blit(self.spawner, (
                self.SPAWNER.y * cell.Cell.SIZE, self.SPAWNER.x * cell.Cell.SIZE))
            self.SCREEN.blit(self.game_hud,
                             self.GAME_HUD_START_POINT)
            self.update()
            self.SCREEN.blit(self.hp, self.HP_POINT)
            self.SCREEN.blit(self.coin, self.COIN_POINT)
            self.SCREEN.blit(self.wave, self.WAVE_POINT)
        else:
            self.SCREEN.blit(self.left_arrow,
                             self.LEVELS_ARROWS_POINTS[1])
            self.SCREEN.blit(self.right_arrow,
                             self.LEVELS_ARROWS_POINTS[0])
            self.SCREEN.blit(self.play_button,
                             self.LEVELS_PLAY_POINTS[0])
            self.SCREEN.blit(self.delete_button,
                             self.LEVELS_DELETE_POINTS[0])
        pygame.display.update()

    def game_process(self):
        """
        Игровой процесс
        """
        if not (global_names.TIMER / 30 - len(
                global_names.MONSTERS) - global_names.WAVE_LONG) % 10:
            self.SPAWNER.spawn()
            global_names.WAVE_NUMBER += 1

        if not global_names.TIMER % 30:
            """
            Создает монстра на карте
            """
            for unit in global_names.MONSTERS:
                if not unit.point:
                    unit.point = 1
                    break

        for unit in global_names.MONSTERS:
            if unit.point:
                self.PLAY, self.LEVELS, self.SPAWNER, self.CASTLE, self.MENU = unit.move(self.CASTLE, self.PLAY, self.LEVELS, self.SPAWNER, self.MENU)

        for tower in global_names.TOWERS:
            if not global_names.TIMER % (
                    (self.towers.TOWER_SPEED[-1] / tower.speed) * 10):
                tower.fire(self.CASTLE)

        global_names.TIMER += 1
        self.draw_window_levels()
