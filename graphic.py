import pygame

import saver
import map
import anims
import global_names

pygame.init()


def create_map():
    global_names.MAP = map.Map()
    for i in range(global_names.MAP.width):
        temp = []
        for j in range(global_names.MAP.length):
            temp.append(anims.cell)
        global_names.MAP.scheme.append(temp)


def set_fps(fps):
    global_names.CLOCK = pygame.time.Clock()
    global_names.CLOCK.tick(fps)


def get_mouse_for_button(pos):
    mouse = pygame.mouse.get_pos()
    if pos[0] <= mouse[0] <= pos[2] and pos[1] <= mouse[1] <= pos[3]:
        return True
    return False


def get_mouse_for_cell():
    global_names.TEMP_CELL = list(pygame.mouse.get_pos())
    global_names.TEMP_CELL[0] = global_names.TEMP_CELL[
                                    0] // global_names.CELL_SIZE
    global_names.TEMP_CELL[1] = global_names.TEMP_CELL[
                                    1] // global_names.CELL_SIZE
    print(global_names.TEMP_CELL)


def create_window():
    global_names.SCREEN = pygame.display.set_mode(global_names.SCREENSIZE, )
    pygame.display.set_caption("TD v1.0")


def key_check_menu():
    for global_names.EVENT in pygame.event.get():
        if global_names.EVENT.type == pygame.QUIT:
            global_names.RUN = False
        if global_names.EVENT.type == pygame.MOUSEBUTTONDOWN:
            if get_mouse_for_button(global_names.MENU_BUTTON_1_POINT[1]):
                global_names.LEVELS = True
                global_names.MENU = False
            if get_mouse_for_button(global_names.MENU_BUTTON_2_POINT[1]):
                global_names.EDITOR = True
                global_names.MENU = False
                create_map()


def draw_window_menu():
    global_names.SCREEN.blit(anims.temp_bg, global_names.ORDINARY_START_POINT)
    global_names.SCREEN.blit(anims.menu_button_level,
                             global_names.MENU_BUTTON_1_POINT[0])
    global_names.SCREEN.blit(anims.menu_button_editor,
                             global_names.MENU_BUTTON_2_POINT[0])
    pygame.display.update()


def key_check_editor():
    for global_names.EVENT in pygame.event.get():
        if global_names.EVENT.type == pygame.QUIT:
            global_names.RUN = False
        if global_names.EVENT.type == pygame.MOUSEBUTTONDOWN:
            if global_names.CELL_MENU:
                if get_mouse_for_button(global_names.CELL_MENU_POINTS[1]):
                    global_names.MAP.scheme[global_names.TEMP_CELL[1]][
                        global_names.TEMP_CELL[0]] = anims.grass
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
        # save map
        if global_names.EVENT.type == pygame.KEYDOWN:
            if global_names.EVENT.key == pygame.K_s:
                saver.save()
                global_names.SAVE = True
                global_names.EDITOR = False
                global_names.MENU = True


def draw_window_editor():
    global_names.MAP.print()
    if global_names.CELL_MENU:
        global_names.SCREEN.blit(anims.cell_menu,
                                 global_names.CELL_MENU_POINTS[0])
    pygame.display.update()
