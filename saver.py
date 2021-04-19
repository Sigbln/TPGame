import pickle
import os

import global_names


def load():
    if os.path.exists(global_names.MY_PATH) and os.path.getsize(
            global_names.MY_PATH) > global_names.EMPTY:
        with open(global_names.MY_PATH, "rb") as f:
            global_names.MAPS_COLLECTION = pickle.load(f)


def convert():
    data = []
    for temp_y in range(global_names.MAP.width):
        temp_data = []
        for temp_x in range(global_names.MAP.length):
            temp_data.append(global_names.DICTIONARY_FROM[
                                 global_names.MAPS_COLLECTION[
                                     global_names.TEMP_ID][temp_y][temp_x]])
        data.append(temp_data)
    return data


def save_after_editor():
    with open("maps/maps.pickle", "wb") as f:
        data = []
        for temp_y in range(global_names.MAP.width):
            temp_data = []
            for temp_x in range(global_names.MAP.length):
                temp_data.append(global_names.DICTIONARY_TO[
                                     global_names.MAP.scheme[temp_y][temp_x]])
            data.append(temp_data)
        global_names.MAPS_COLLECTION.append(data)
        pickle.dump(global_names.MAPS_COLLECTION, f)


def save():
    with open("maps/maps.pickle", "wb") as f:
        pickle.dump(global_names.MAPS_COLLECTION, f)
