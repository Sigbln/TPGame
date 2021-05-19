import pygame

import graphic
import saver

graphic = graphic.Graphic()
saver = saver.saver()

graphic.create_window()

saver.load()

while graphic.RUN:
    graphic.set_fps(graphic.FPS)
    if graphic.MENU:
        graphic.key_check_menu()
        graphic.draw_window_menu()
    if graphic.EDITOR:
        graphic.key_check_editor()
        graphic.draw_window_editor()
    if graphic.LEVELS:
        if graphic.PLAY:
            graphic.game_process()
        graphic.key_check_levels()
        graphic.draw_window_levels()

saver.save()

pygame.quit()
