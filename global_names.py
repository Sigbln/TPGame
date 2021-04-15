import anims

SCREENSIZE = (1080, 720)
FPS = 30
ORDINARY_START_POINT = (0, 0)
SAVE_START_POINT = (415, 320)
CELL_MENU_POINTS = (
    (455, 335), (458, 341, 498, 381), (501, 341, 541, 381),
    (544, 341, 584, 381),
    (587, 341, 627, 381))
CELL_SIZE = 40
MENU_BUTTON_1_POINT = ((440, 300), (440, 300, 640, 375))
MENU_BUTTON_2_POINT = ((440, 405), (440, 405, 640, 480))
EVENT = None
CLOCK = None
SCREEN = None

MY_PATH = "maps/maps.pickle"
# temp
TEMP_CELL = None
TEMP_ID = None

# цвета
WHITE = (255, 255, 255)

MAPS_COLLECTION = []

# flags
RUN = True
MENU = True
EDITOR = False
LEVELS = False
CELL_MENU = False
SAVE = False

MAP = None

ANIM_COUNT = 0
EMPTY = 0
TIME_SAVE = 30

DICTIONARY_TO = {anims.cell: 1, anims.road: 2, anims.spawner: 3,
                 anims.castle: 4, anims.grass: 5}
DICTIONARY_FROM = {1: anims.cell, 2: anims.road, 3: anims.spawner,
                   4: anims.castle, 5: anims.grass}


