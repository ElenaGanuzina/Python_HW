"""
Напишите функцию, которая ищет json файлы в указанной директории
и сохраняет их содержимое в виде одноименных pickle файлов.
"""

import json
import pickle
import os

__all__ = ['pickle_reader']


def pickle_reader(dir_):
    json_files = [i for i in os.listdir(dir_) if i.endswith('.json')]
    for file in json_files:
        with (open(os.path.join(dir_, file), 'r', encoding='utf-8') as f,
              open(os.path.join(dir_, file.strip('.json') + '.pickle'), 'wb') as pf):

            pickle.dump(json.load(f), pf)


if __name__ == '__main__':
    pickle_reader(os.getcwd())
    with open('seminar_8/user.pickle', 'rb') as f:
        print(pickle.load(f))