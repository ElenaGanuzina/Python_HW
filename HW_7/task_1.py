"""
Задание 1.

? Генерируйте файлы в указанную директорию — отдельный параметр функции.
? Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
? Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

from random import randint, choices
import os

__all__ = ['task_1']

LETTERS = "abcdefghijklmnopqrstuvwxyz"


def check_dir(my_dir):
    if my_dir not in os.listdir():
        print("There is no such directory. Do you want to create one? Y/N")
        answer = input()
        if answer == 'Y':
            os.mkdir(my_dir)
            os.chdir(os.path.join(os.getcwd(), my_dir))
        else:
            print("OK, you're the boss.")
    else:
        os.chdir(os.path.join(os.getcwd(), my_dir))


def create_files(extension, name_min=6, name_max=30, byte_min=256, byte_max=4096, file_num=42):
    for _ in range(file_num):
        name = ''.join(choices(LETTERS, k=randint(name_min, name_max))) + '.' + extension
        if name in os.listdir():
            expand = 1
            while True:
                data = name.split(".")
                new_name = data[0] + str(expand) + "." + data[1]
                if new_name in os.listdir():
                    expand += 1
                    continue
                else:
                    name = new_name
                    break
        with open(name, 'wb') as f:
            data = os.urandom(randint(byte_min, byte_max))
            f.write(data)


def create_dif_files(**kwargs):
    for extension, num in kwargs.items():
        create_files(extension, file_num=num)


if __name__ == '__main__':
    # create_files('txt')
    check_dir("My new directory")
    create_dif_files(png=3, pdf=2, bin=4)