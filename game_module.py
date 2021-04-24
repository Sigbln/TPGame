import global_names
import graphic


def way_to_move():
    special_map = global_names.MAPS_COLLECTION[global_names.TEMP_ID]
    lab = []

    n = global_names.MAP.width
    m = global_names.MAP.length

    for i in range(n):
        line = []
        for k in range(len(special_map[i])):
            if special_map[i][k] == 1 or special_map[i][k] == 5:
                line.append(-1)
            elif special_map[i][k] == 2:
                line.append(0)
            elif special_map[i][k] == 4:
                global_names.CASTLE.x = i
                global_names.CASTLE.y = k
                line.append(0)
            elif special_map[i][k] == 3:
                global_names.SPAWNER.x = i
                global_names.SPAWNER.y = k
                line.append(0)
            else:
                line.append(special_map[i][k])
        lab.append(line)

    finalout = voln(global_names.SPAWNER.x, global_names.SPAWNER.y, 1, n, m, lab)
    if lab[global_names.CASTLE.x][global_names.CASTLE.y] > 0:
        path = way(global_names.SPAWNER.y, global_names.SPAWNER.x, global_names.CASTLE.y, global_names.CASTLE.x,
                   finalout)
        path = path[::-1]
        global_names.PATH = path
    else:
        raise FileExistsError("Wrong way from spawner to castle")


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
    n = global_names.MAP.width
    m = global_names.MAP.length

    path = [[x2, y2]]
    while (x1, y1) != (x2, y2):
        if x2 > 0 and lab[y2][x2 - 1] == lab[y2][x2] - 1:
            x2, y2 = x2 - 1, y2
        elif x2 < m - 1 and lab[y2][x2 + 1] == lab[y2][x2] - 1:
            x2, y2 = x2 + 1, y2
        elif y2 > 0 and lab[y2 - 1][x2] == lab[y2][x2] - 1:
            x2, y2 = x2, y2 - 1
        elif y2 < n - 1 and lab[y2 + 1][x2] == lab[y2][x2] - 1:
            x2, y2 = x2, y2 + 1
        path.append([x2, y2])
    return path


def monsters_spawn():
    for unit in global_names.MONSTERS:
        if not unit.point:
            unit.point = 1
            break


def game_process():
    if not (global_names.TIMER / 30 - len(global_names.MONSTERS) - global_names.WAVE_LONG) % 10:
        global_names.SPAWNER.spawn()
        global_names.WAVE_NUMBER += 1

    if not global_names.TIMER % 30:
        monsters_spawn()

    for unit in global_names.MONSTERS:
        unit.move()

    for tower in global_names.TOWERS:
        if not global_names.TIMER % ((global_names.TOWER_SPEED[-1] / tower.speed) * 10):
            tower.fire()

    global_names.TIMER += 1
    graphic.draw_window_levels()
