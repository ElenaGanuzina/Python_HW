"""
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
* имя файла без расширения или название каталога,
* расширение, если это файл,
* флаг каталога,
* название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""
import logging
import os
from collections import namedtuple
from functools import wraps

FORMAT = '{levelname:<8} - {asctime}. {msg}'
logging.basicConfig(filename='log.log', format=FORMAT, style='{', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'The contents of the directory {args} are: \n')
        for item in result:
            logger.info(f'{item.name}, {item.parent}, {item.extension}, {item.flag}')
        return result

    return wrapper


@log
def dir_data(string_path):
    info = []
    for dir_path, dir_names, files in os.walk(string_path):
        for elem in dir_names:
            info.append({"name": elem, "parent": os.path.basename(dir_path), 'extension': None, 'flag': True})
        for item in files:
            info.append({"name": item, "parent": os.path.basename(dir_path),
                         'extension': item.split(".")[-1], "flag": False})

    Element = namedtuple('Directory', ['name', 'parent', 'extension', 'flag'])
    result = []
    for item in info:
        item = Element(**item)
        result.append(item)
    return result


if __name__ == '__main__':
    dir_ = "Enter path to your directiory."
    dir_data(dir_)
