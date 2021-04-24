import anims

import cell

# font
FONT_SIZE = 40
HP_POINT = (950, 607)
COIN_POINT = (1010, 650)
WAVE_POINT = (1000, 690)

SCREENSIZE = (1080, 720)
FPS = 30
ORDINARY_START_POINT = (0, 0)
SAVE_START_POINT = (415, 320)
CELL_MENU_POINTS = (
    (455, 335), (458, 341, 498, 381), (501, 341, 541, 381),
    (544, 341, 584, 381),
    (587, 341, 627, 381))
LEVELS_ARROWS_POINTS = (
    (0, 360), (1040, 360), (0, 360, 40, 400), (1040, 360, 1080, 400))
LEVELS_PLAY_POINTS = ((300, 605), (300, 605, 500, 680))
LEVELS_DELETE_POINTS = ((580, 605), (580, 605, 780, 680))
CELL_SIZE = 40
MENU_BUTTON_1_POINT = ((440, 300), (440, 300, 640, 375))
MENU_BUTTON_2_POINT = ((440, 405), (440, 405, 640, 480))
GAME_HUD_START_POINT = (880, 600)
EVENT = None
CLOCK = None
SCREEN = None

MY_PATH = "maps/maps.pickle"
# temp
TEMP_CELL = None
TEMP_ID = 0

# цвета
WHITE = (255, 255, 255)

MAPS_COLLECTION = []

# flags
RUN = True
MENU = True
EDITOR = False
LEVELS = False
CELL_MENU = False
PLAY = False
SAVE = False

DAMAGED_MONSTER = False
DAMAGED_X = None
DAMAGED_Y = None

MAP = None

ANIM_COUNT = 0
EMPTY = 0
TIME_SAVE = 30

DICTIONARY_TO = {anims.grass: 1, anims.road: 2, anims.spawner: 3,
                 anims.castle: 4, anims.grass: 5}
DICTIONARY_FROM = {1: anims.grass, 2: anims.road, 3: anims.spawner,
                   4: anims.castle, 5: anims.grass}

# game process
TIMER = 0
SPAWNER = cell.Spawner(0, 0, 10)
CASTLE = cell.Castle(0, 0, 100, 5)
MONSTERS = []
PATH = []
WAVE_LONG = 20
MONSTERS_NAMES = ["Bugbear", "Hobgoglin", "Runner"]
MONSTERS_COST = {"Bugbear": 1, "Hobgoglin": 1, "Runner": 1}
TOWERS = []
TOWER_POWER = [2]
TOWER_SPEED = [1]
TOWER_RADIUS = [100]
TOWER_CREATING_COST = 20
TOWER_REMOVING_COST = 10
WAVE_NUMBER = 1
