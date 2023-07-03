"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os

__all__ = ['sem_07_5']

DIR = {"Pictures": ["jpeg", "jpg", "png"], "Documents": ["txt", "doc", "pdf", "bin"]}


def group_files(dir_):
    files = [file for file in os.listdir(dir_) if os.path.isfile(file)]
    for fold, extension in DIR.items():
        if fold not in os.listdir():
            os.mkdir(fold)
        for file in files:
            if file.split('.')[1] in extension:
                os.replace(file, os.path.join(dir_, fold, file))


if __name__ == '__main__':
    group_files(os.getcwd())