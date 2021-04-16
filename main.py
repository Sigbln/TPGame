import pygame

import map
#import game_module
import global_names
import graphic
import saver

graphic.create_window()

saver.load()

print(global_names.MAPS_COLLECTION[2])

while global_names.RUN:
    graphic.set_fps(global_names.FPS)
    if global_names.MENU:
        graphic.key_check_menu()
        graphic.draw_window_menu()
    if global_names.EDITOR:
        graphic.key_check_editor()
        graphic.draw_window_editor()
    if global_names.LEVELS:
        graphic.key_check_levels()
        graphic.draw_window_levels()


#game_module.main()

saver.save()

pygame.quit()
