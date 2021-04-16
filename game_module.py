import collections
import random
import global_names
import cell
import monster

def way_to_move():
    rdl = [[3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    lab = []

    n = 18
    m = 27

    for i in range(n):
        stroka = []
        for k in range(len(rdl[i])):
            if rdl[i][k] == 1 or rdl[i][k] == 5:
                stroka.append(-1)
            elif rdl[i][k] == 2:
                stroka.append(0)
            elif rdl[i][k] == 4:
                global_names.CASTLE.x = i
                global_names.CASTLE.y = k
                stroka.append(0)
            elif rdl[i][k] == 3:
                global_names.SPAWNER.x = i
                global_names.SPAWNER.y = k
                stroka.append(0)
            else:
                stroka.append(rdl[k][i])
        lab.append(stroka)

    finalout = voln(global_names.SPAWNER.x, global_names.SPAWNER.y, 1, n, m, lab)
    if lab[global_names.CASTLE.x][global_names.CASTLE.y] > 0:
        path = way(global_names.SPAWNER.x, global_names.SPAWNER.y, global_names.CASTLE.x, global_names.CASTLE.y, finalout)
        path = path[::-1]
        global_names.PATH = path
    else:
        print("Error")


def voln(x, y, cur, n, m, lab):
    lab[x][y] = cur
    if y + 1 < m:
        if lab[x][y + 1] == 0 or (lab[x][y + 1] != -1 and lab[x][y + 1] > cur + 1):
            voln(x, y + 1, cur + 1, n, m, lab)
    if x + 1 < n:
        if lab[x + 1][y] == 0 or (lab[x + 1][y] != -1 and lab[x + 1][y] > cur + 1):
            voln(x + 1, y, cur + 1, n, m, lab)
    if x - 1 >= 0:
        if lab[x - 1][y] == 0 or (lab[x - 1][y] != -1 and lab[x - 1][y] > cur + 1):
            voln(x - 1, y, cur + 1, n, m, lab)
    if y - 1 >= 0:
        if lab[x][y - 1] == 0 or (lab[x][y - 1] != -1 and lab[x][y - 1] > cur + 1):
            voln(x, y - 1, cur + 1, n, m, lab)
    return lab


def way(x1, y1, x2, y2, lab):
    n = 18
    m = 27
    path = [[x2, y2]]
    while (x1, y1) != (x2, y2):
        if x2 > 0 and lab[y2][x2 - 1] == lab[y2][x2] - 1:
            x2, y2 = x2 - 1, y2
        elif x2 < n - 1 and lab[y2][x2 + 1] == lab[y2][x2] - 1:
            x2, y2 = x2 + 1, y2
        elif y2 > 0 and lab[y2 - 1][x2] == lab[y2][x2] - 1:
            x2, y2 = x2, y2 - 1
        elif y2 < m - 1 and lab[y2 + 1][x2] == lab[y2][x2] - 1:
            x2, y2 = x2, y2 + 1
        path.append([x2, y2])
    return path

def monsters_move(monster):
    if monster.point:
        if global_names.PATH[monster.point + 1][0] - global_names.PATH[monster.point][0]:
            if monster.x + monster.speed < 40 * global_names.PATH[monster.point]:
                monster.x += monster.speed
            else:
                monster.x = monster.speed - (40 - monster.x)
                monster.point += 1
                if monster.point == len(global_names.PATH):
                    monster.finish()
        else:
            if monster.y + monster.speed < 40 * global_names.PATH[monster.point]:
                monster.y += monster.speed
            else:
                monster.y = monster.speed - (40 - monster.y)
                monster.point += 1
                if monster.point == len(global_names.PATH):
                    monster.finish()

    return monster

def wave_generate():
    for i in range(0, global_names.SPAWNER.power):
        global_names.MONSTERS.append(monster.Monster[random.randint(0, 2)])

def monsters_spawn():
    for i in global_names.MONSTERS:
        if not i.point:
            i.point = 1
            break


def game_process():
    if not global_names.TIMER % 30:
        monsters_spawn()
    if not (global_names.TIMER / 30 - len(global_names.MONSTERS) - global_names.WAVE_LONG) % 10:
        wave_generate()

    for unit in global_names.MONSTERS:
        monsters_move(unit)

    global_names.TIMER += 1
    pass


way = way_to_move()
