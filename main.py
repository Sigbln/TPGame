import pygame

import map
import global_names
import graphic
import saver

graphic.create_window()
saver.load()

while global_names.RUN:
    graphic.set_fps(global_names.FPS)
    if global_names.MENU:
        graphic.key_check_menu()
        graphic.draw_window_menu()
    if global_names.EDITOR:
        graphic.key_check_editor()
        graphic.draw_window_editor()

pygame.quit()
