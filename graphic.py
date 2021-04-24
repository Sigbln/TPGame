import pygame

import hud
import anims
import cell
import game_module
import global_names
import map
import saver

pygame.init()


def create_map():
    """
    Создает карту, заполненную картинками травы если действие происходит в редакторе и
    если действие происходит в меню выбора уровня создает карту которая находится в массиве
    карт под номером TEMP_ID
    """
    global_names.MAP = map.Map()
    for i in range(global_names.MAP.width):
        temp = []
        for j in range(global_names.MAP.length):
            temp.append(anims.grass)
            # temp2.append(5)
        global_names.MAP.scheme.append(temp)
    if global_names.LEVELS:
        global_names.MAP.scheme = saver.convert()


def set_fps(fps):
    global_names.CLOCK = pygame.time.Clock()
    global_names.CLOCK.tick(fps)


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


def get_mouse_for_cell():
    """
    По нажатию мышки получает на какую клетку было совершено нажатие
    """
    global_names.TEMP_CELL = list(pygame.mouse.get_pos())
    global_names.TEMP_CELL[0] = global_names.TEMP_CELL[
                                    0] // global_names.CELL_SIZE
    global_names.TEMP_CELL[1] = global_names.TEMP_CELL[
                                    1] // global_names.CELL_SIZE


def create_window():
    global_names.SCREEN = pygame.display.set_mode(global_names.SCREENSIZE, )
    pygame.display.set_caption("TD v1.0")


def key_check_menu():
    """
    Проверяет нажатие кнопок в меню и реагирует на них
    """
    for global_names.EVENT in pygame.event.get():
        if global_names.EVENT.type == pygame.QUIT:
            global_names.RUN = False
        if global_names.EVENT.type == pygame.MOUSEBUTTONDOWN:
            if get_mouse_for_button(global_names.MENU_BUTTON_1_POINT[1]):
                global_names.LEVELS = True
                global_names.MENU = False
                create_map()
            if get_mouse_for_button(global_names.MENU_BUTTON_2_POINT[1]):
                global_names.EDITOR = True
                global_names.MENU = False
                create_map()


def draw_window_menu():
    """
    Отрисовывает окно меню
    """
    global_names.SCREEN.blit(anims.temp_bg, global_names.ORDINARY_START_POINT)
    global_names.SCREEN.blit(anims.menu_button_level,
                             global_names.MENU_BUTTON_1_POINT[0])
    global_names.SCREEN.blit(anims.menu_button_editor,
                             global_names.MENU_BUTTON_2_POINT[0])
    pygame.display.update()


def key_check_editor():
    """
    Проверяет нажатие кнопок в редакторе и реагирует на них
    """
    for global_names.EVENT in pygame.event.get():
        if global_names.EVENT.type == pygame.QUIT:
            global_names.RUN = False
        if global_names.EVENT.type == pygame.MOUSEBUTTONDOWN:
            # менюшка с выбором клеток для карты
            if global_names.CELL_MENU:
                # земля
                if get_mouse_for_button(global_names.CELL_MENU_POINTS[1]):
                    global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                        global_names.TEMP_CELL[0]] = anims.grass
                # дорога
                elif get_mouse_for_button(global_names.CELL_MENU_POINTS[2]):
                    global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                        global_names.TEMP_CELL[0]] = anims.road
                elif get_mouse_for_button(global_names.CELL_MENU_POINTS[3]):
                    global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                        global_names.TEMP_CELL[0]] = anims.spawner
                elif get_mouse_for_button(global_names.CELL_MENU_POINTS[4]):
                    global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                        global_names.TEMP_CELL[0]] = anims.castle
                global_names.CELL_MENU = False
            else:
                get_mouse_for_cell()
                global_names.CELL_MENU = True
        # save_after_editor map
        if global_names.EVENT.type == pygame.KEYDOWN:
            if global_names.EVENT.key == pygame.K_s:
                saver.save_after_editor()
                global_names.EDITOR = False
                global_names.MENU = True


def draw_window_editor():
    """
    Отрисовывает окно редактора
    """
    global_names.MAP.print()
    if global_names.CELL_MENU:
        global_names.SCREEN.blit(anims.cell_menu,
                                 global_names.CELL_MENU_POINTS[0])
    pygame.display.update()


def key_check_levels():
    """
    Проверяет нажатие кнопок в меню выбора уровня и в самой игре, реагирует на них
    """
    for global_names.EVENT in pygame.event.get():
        if global_names.EVENT.type == pygame.QUIT:
            global_names.RUN = False
        if global_names.EVENT.type == pygame.MOUSEBUTTONDOWN:
            if global_names.PLAY:
                get_mouse_for_cell()
                if global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                    global_names.TEMP_CELL[0]] == anims.grass:
                    # ставит башню там где был произведен клик мышкой
                    if global_names.CASTLE.money >= global_names.TOWER_CREATING_COST:
                        global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                            global_names.TEMP_CELL[0]] = anims.tower
                        global_names.TOWERS.append(
                            cell.Tower(global_names.TEMP_CELL[0],
                                       global_names.TEMP_CELL[1],
                                       global_names.TOWER_POWER[0],
                                       global_names.TOWER_SPEED[0],
                                       global_names.TOWER_RADIUS[0]))
                        global_names.CASTLE.money -= global_names.TOWER_CREATING_COST
                    else:
                        print("Not enough money")
                elif global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                    global_names.TEMP_CELL[0]] == anims.tower:
                    # убирает башню если по ней был произведен клик мышкой
                    global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                        global_names.TEMP_CELL[0]] = anims.grass
                    for tower in global_names.TOWERS:
                        if tower.x == global_names.TEMP_CELL[0] and tower.y == \
                                global_names.TEMP_CELL[1]:
                            global_names.TOWERS.remove(tower)
                            global_names.CASTLE.money += global_names.TOWER_REMOVING_COST
                pass
            else:
                # стрелка влево
                if get_mouse_for_button(global_names.LEVELS_ARROWS_POINTS[2]):
                    print(len(global_names.MAPS_COLLECTION))
                    if global_names.TEMP_ID in range(1,
                                                     len(global_names.MAPS_COLLECTION)):
                        global_names.TEMP_ID -= 1
                        global_names.MAP.scheme = saver.convert()
                # стрелка вправо
                elif get_mouse_for_button(
                        global_names.LEVELS_ARROWS_POINTS[3]):
                    if global_names.TEMP_ID in range(
                            len(global_names.MAPS_COLLECTION) - 1):
                        global_names.TEMP_ID += 1
                        global_names.MAP.scheme = saver.convert()
                        print("p")
                # кнопка начала игры
                elif get_mouse_for_button(global_names.LEVELS_PLAY_POINTS[1]):
                    global_names.PLAY = True
                    game_module.way_to_move()
                # кнопка удаления карты
                elif get_mouse_for_button(
                        global_names.LEVELS_DELETE_POINTS[1]):
                    global_names.MAPS_COLLECTION.pop(global_names.TEMP_ID)
                    global_names.TEMP_ID = global_names.EMPTY
                    global_names.MAP.scheme = saver.convert()


def draw_window_levels():
    """
    Отрисоввывает окно выбора уровня или окно самой игры
    """
    global_names.MAP.print()
    if global_names.PLAY:
        for unit in global_names.MONSTERS:
            if not unit.injured:
                global_names.SCREEN.blit(anims.monster, (
                    unit.y + global_names.PATH[unit.point][0] * 40,
                    unit.x + global_names.PATH[unit.point][1] * 40))
            else:
                global_names.SCREEN.blit(anims.damaged_monster, (
                    unit.y + global_names.PATH[unit.point][0] * 40,
                    unit.x + global_names.PATH[unit.point][1] * 40))

        global_names.SCREEN.blit(anims.spawner, (
            global_names.SPAWNER.y * 40, global_names.SPAWNER.x * 40))
        global_names.SCREEN.blit(anims.game_hud,
                                 global_names.GAME_HUD_START_POINT)
        hud.update()
        global_names.SCREEN.blit(hud.hp, global_names.HP_POINT)
        global_names.SCREEN.blit(hud.coin, global_names.COIN_POINT)
        global_names.SCREEN.blit(hud.wave, global_names.WAVE_POINT)
    else:
        global_names.SCREEN.blit(anims.left_arrow,
                                 global_names.LEVELS_ARROWS_POINTS[1])
        global_names.SCREEN.blit(anims.right_arrow,
                                 global_names.LEVELS_ARROWS_POINTS[0])
        global_names.SCREEN.blit(anims.play_button,
                                 global_names.LEVELS_PLAY_POINTS[0])
        global_names.SCREEN.blit(anims.delete_button,
                                 global_names.LEVELS_DELETE_POINTS[0])
    pygame.display.update()
