import pygame

import global_names

pygame.init()

font = pygame.font.Font(None, global_names.FONT_SIZE)

hp = None
coin = None
wave = None


def update():
    """
    Обновляет значение hp, coin, wave
    """
    global hp, coin, wave
    hp = font.render(str(global_names.CASTLE.hp), True, global_names.WHITE)
    coin = font.render(str(global_names.CASTLE.money), True,
                       global_names.WHITE)
    wave = font.render(str(global_names.WAVE_NUMBER), True, global_names.WHITE)
