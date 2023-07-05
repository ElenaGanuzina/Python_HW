"""
Задание 2.

Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов.

* При переименовании в конце имени добавляется порядковый номер.

* принимать в качестве аргумента расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.

* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

"""

import os

__all__ = ['task_2']


def file_rename(dir_path, new_name, original_ext, new_ext):
    os.chdir(dir_path)
    position = 1
    for file in os.listdir():
        if file.endswith(original_ext):
            os.rename(file, f'{file.split(".")[0]}_{new_name}_{position}.{new_ext}')
            position += 1


if __name__ == "__main__":
    # dir_path = ""
    file_rename(dir_path, "staff", "png", "jpg")
