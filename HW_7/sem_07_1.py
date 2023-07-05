"""
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""

from random import randint
from random import uniform

__all__ = ['sem_07_1']


def write_file(filename, row):
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(row):
            a, b = randint(-1000, 1000), uniform(-1000, 1000)
            f.write(f'{a}|{b}\n')


if __name__ == '__main__':
    write_file('numbers.txt', 5)
