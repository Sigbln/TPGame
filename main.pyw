import pygame

import global_names
import game_module
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
    if global_names.LEVELS:
        if global_names.PLAY:
            game_module.game_process()
        graphic.key_check_levels()
        graphic.draw_window_levels()

saver.save()

pygame.quit()
