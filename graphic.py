import pygame

import hud
import cell
import game_module
import global_names
import map
import saver

pygame.init()


class Graphic:

    def __init__(self):
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

    def create_map(self):

        """
        Создает карту, заполненную картинками травы если действие происходит в редакторе и
        если действие происходит в меню выбора уровня создает карту которая находится в массиве
        карт под номером TEMP_ID
        """

        global_names.MAP = map.Map()
        for i in range(global_names.MAP.width):
            temp = []
            for j in range(global_names.MAP.length):
                temp.append(self.grass)
            global_names.MAP.scheme.append(temp)
        if global_names.LEVELS:
            global_names.MAP.scheme = saver.convert(self.DICTIONARY_FROM)

    @staticmethod
    def set_fps(fps):
        global_names.CLOCK = pygame.time.Clock()
        global_names.CLOCK.tick(fps)

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

    @staticmethod
    def get_mouse_for_cell():
        """
        По нажатию мышки получает на какую клетку было совершено нажатие
        """
        global_names.TEMP_CELL = list(pygame.mouse.get_pos())
        global_names.TEMP_CELL[0] = global_names.TEMP_CELL[
                                        0] // global_names.CELL_SIZE
        global_names.TEMP_CELL[1] = global_names.TEMP_CELL[
                                        1] // global_names.CELL_SIZE

    @staticmethod
    def create_window():
        global_names.SCREEN = pygame.display.set_mode(
            global_names.SCREENSIZE, )
        pygame.display.set_caption("TD v1.0")

    def key_check_menu(self):
        """
        Проверяет нажатие кнопок в меню и реагирует на них
        """
        for global_names.EVENT in pygame.event.get():
            if global_names.EVENT.type == pygame.QUIT:
                global_names.RUN = False
            if global_names.EVENT.type == pygame.MOUSEBUTTONDOWN:
                if self.get_mouse_for_button(
                        global_names.MENU_BUTTON_1_POINT[1]):
                    global_names.LEVELS = True
                    global_names.MENU = False
                    self.create_map()
                if self.get_mouse_for_button(
                        global_names.MENU_BUTTON_2_POINT[1]):
                    global_names.EDITOR = True
                    global_names.MENU = False
                    self.create_map()

    def draw_window_menu(self):
        """
        Отрисовывает окно меню
        """
        global_names.SCREEN.blit(self.temp_bg,
                                 global_names.ORDINARY_START_POINT)
        global_names.SCREEN.blit(self.menu_button_level,
                                 global_names.MENU_BUTTON_1_POINT[0])
        global_names.SCREEN.blit(self.menu_button_editor,
                                 global_names.MENU_BUTTON_2_POINT[0])
        pygame.display.update()

    def key_check_editor(self):
        """
        Проверяет нажатие кнопок в редакторе и реагирует на них
        """
        for global_names.EVENT in pygame.event.get():
            if global_names.EVENT.type == pygame.QUIT:
                global_names.RUN = False
            elif global_names.EVENT.type == pygame.MOUSEBUTTONDOWN:
                # менюшка с выбором клеток для карты
                if global_names.CELL_MENU:
                    # земля
                    if self.get_mouse_for_button(
                            global_names.CELL_MENU_POINTS[1]):
                        global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                            global_names.TEMP_CELL[0]] = self.grass
                    # дорога
                    elif self.get_mouse_for_button(
                            global_names.CELL_MENU_POINTS[2]):
                        global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                            global_names.TEMP_CELL[0]] = self.road
                    elif self.get_mouse_for_button(
                            global_names.CELL_MENU_POINTS[3]):
                        global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                            global_names.TEMP_CELL[0]] = self.spawner
                    elif self.get_mouse_for_button(
                            global_names.CELL_MENU_POINTS[4]):
                        global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                            global_names.TEMP_CELL[0]] = self.castle
                    global_names.CELL_MENU = False
                else:
                    self.get_mouse_for_cell()
                    global_names.CELL_MENU = True
            # save_after_editor map
            if global_names.EVENT.type == pygame.KEYDOWN:
                if global_names.EVENT.key == pygame.K_s:
                    saver.save_after_editor(self.DICTIONARY_TO)
                    global_names.EDITOR = False
                    global_names.MENU = True

    def draw_window_editor(self):
        """
        Отрисовывает окно редактора
        """
        global_names.MAP.print()
        if global_names.CELL_MENU:
            global_names.SCREEN.blit(self.cell_menu,
                                     global_names.CELL_MENU_POINTS[0])
        pygame.display.update()

    def key_check_levels(self):
        """
        Проверяет нажатие кнопок в меню выбора уровня и в самой игре, реагирует на них
        """
        for global_names.EVENT in pygame.event.get():
            if global_names.EVENT.type == pygame.QUIT:
                global_names.RUN = False
            if global_names.EVENT.type == pygame.MOUSEBUTTONDOWN:
                if global_names.PLAY:
                    self.get_mouse_for_cell()
                    if global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                        global_names.TEMP_CELL[0]] == self.grass:
                        # ставит башню там где был произведен клик мышкой
                        if global_names.CASTLE.money >= global_names.TOWER_CREATING_COST:
                            global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                                global_names.TEMP_CELL[0]] = self.tower
                            global_names.TOWERS.append(
                                cell.Tower(global_names.TEMP_CELL[0],
                                           global_names.TEMP_CELL[1],
                                           global_names.TOWER_POWER[0],
                                           global_names.TOWER_SPEED[0],
                                           global_names.TOWER_RADIUS[0]))
                            global_names.CASTLE.money -= global_names.TOWER_CREATING_COST
                    elif global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                        global_names.TEMP_CELL[0]] == self.tower:
                        # убирает башню если по ней был произведен клик мышкой
                        global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                            global_names.TEMP_CELL[0]] = self.grass
                        for tower in global_names.TOWERS:
                            if tower.x == global_names.TEMP_CELL[
                                0] and tower.y == \
                                    global_names.TEMP_CELL[1]:
                                global_names.TOWERS.remove(tower)
                                global_names.CASTLE.money += global_names.TOWER_REMOVING_COST
                    pass
                else:
                    # стрелка влево
                    if self.get_mouse_for_button(
                            global_names.LEVELS_ARROWS_POINTS[2]):
                        print(len(global_names.MAPS_COLLECTION))
                        if global_names.TEMP_ID in range(1,
                                                         len(global_names.MAPS_COLLECTION)):
                            global_names.TEMP_ID -= 1
                            global_names.MAP.scheme = saver.convert(
                                self.DICTIONARY_FROM)
                    # стрелка вправо
                    elif self.get_mouse_for_button(
                            global_names.LEVELS_ARROWS_POINTS[3]):
                        if global_names.TEMP_ID in range(
                                len(global_names.MAPS_COLLECTION) - 1):
                            global_names.TEMP_ID += 1
                            global_names.MAP.scheme = saver.convert(
                                self.DICTIONARY_FROM)
                            print("p")
                    # кнопка начала игры
                    elif self.get_mouse_for_button(
                            global_names.LEVELS_PLAY_POINTS[1]):
                        global_names.PLAY = True
                        game_module.way_to_move()
                    # кнопка удаления карты
                    elif self.get_mouse_for_button(
                            global_names.LEVELS_DELETE_POINTS[1]):
                        global_names.MAPS_COLLECTION.pop(global_names.TEMP_ID)
                        global_names.TEMP_ID = global_names.EMPTY
                        global_names.MAP.scheme = saver.convert(
                            self.DICTIONARY_FROM)

    def draw_window_levels(self):
        """
        Отрисоввывает окно выбора уровня или окно самой игры
        """
        global_names.MAP.print()
        if global_names.PLAY:
            for unit in global_names.MONSTERS:
                if not unit.injured:
                    global_names.SCREEN.blit(self.monster, (
                        unit.y + global_names.PATH[unit.point][0] * 40,
                        unit.x + global_names.PATH[unit.point][1] * 40))
                else:
                    global_names.SCREEN.blit(self.damaged_monster, (
                        unit.y + global_names.PATH[unit.point][0] * 40,
                        unit.x + global_names.PATH[unit.point][1] * 40))

            global_names.SCREEN.blit(self.spawner, (
                global_names.SPAWNER.y * 40, global_names.SPAWNER.x * 40))
            global_names.SCREEN.blit(self.game_hud,
                                     global_names.GAME_HUD_START_POINT)
            hud.update()
            global_names.SCREEN.blit(hud.hp, global_names.HP_POINT)
            global_names.SCREEN.blit(hud.coin, global_names.COIN_POINT)
            global_names.SCREEN.blit(hud.wave, global_names.WAVE_POINT)
        else:
            global_names.SCREEN.blit(self.left_arrow,
                                     global_names.LEVELS_ARROWS_POINTS[1])
            global_names.SCREEN.blit(self.right_arrow,
                                     global_names.LEVELS_ARROWS_POINTS[0])
            global_names.SCREEN.blit(self.play_button,
                                     global_names.LEVELS_PLAY_POINTS[0])
            global_names.SCREEN.blit(self.delete_button,
                                     global_names.LEVELS_DELETE_POINTS[0])
        pygame.display.update()

    def game_process(self):
        """
        Игровой процесс
        """
        if not (global_names.TIMER / 30 - len(
                global_names.MONSTERS) - global_names.WAVE_LONG) % 10:
            global_names.SPAWNER.spawn()
            global_names.WAVE_NUMBER += 1

        if not global_names.TIMER % 30:
            game_module.monsters_spawn()

        for unit in global_names.MONSTERS:
            if unit.point:
                unit.move()

        for tower in global_names.TOWERS:
            if not global_names.TIMER % (
                    (global_names.TOWER_SPEED[-1] / tower.speed) * 10):
                tower.fire()

        global_names.TIMER += 1
        self.draw_window_levels()
