"""
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса.
"""

import math
import csv
import os
from functools import wraps
from random import randint
import json

__all__ = ['quadratic_equation']


def coefficients_gen():
    """Generates coefficients for quadratic equation in range from -10 to 10 and writes them into a csv-file."""
    MIN_STR = 100
    MAX_STR = 1000
    with open('coefficients.csv', 'w', newline='') as f:
        data = []
        for _ in range(MIN_STR, MAX_STR + 1):
            a, b, c = [randint(-10, 10) for _ in range(3)]
            data.append({'a': a, 'b': b, 'c': c})

        writer = csv.DictWriter(f, fieldnames=['a', 'b', 'c'], delimiter=" ", quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        writer.writerows(data)


def get_coefficients(func):
    coefficients_gen()

    @wraps(func)
    def wrapper():
        with open('coefficients.csv', 'r', newline='') as f:
            csv_file = csv.DictReader(f, delimiter=' ', fieldnames=('a', 'b', 'c'), quoting=csv.QUOTE_NONNUMERIC)
            number_list = []
            for i, row in enumerate(csv_file):
                if i != 0:
                    number_list.append(row)
                    a, b, c = [i for i in row.values()]
                    solution = func(a, b, c)
                    yield {'a': a, 'b': b, 'c': c, 'solution': solution}

    return wrapper


def info_to_json(func):
    file_name = func.__name__ + '.json'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            result = json.load(f)
    else:
        result = []

    def wrapper(*args, **kwargs):
        with open(file_name, 'w', encoding='utf-8') as f_json:
            solution = func(*args, **kwargs)
            for item in solution:
                result.append(item)
            json.dump(result, f_json, indent=1)

    return wrapper


@info_to_json
@get_coefficients
def quadratic_equation(*args, **kwargs) -> tuple or int or float or None:
    """Finds possible solutions (except complex numbers) for a quadratic equation."""
    a, b, c = args
    if a == 0:
        return None
    else:
        d = b ** 2 - 4 * a * c
        if d == 0:
            return round(-b / (2 * a), 4)
        elif d < 0:
            return None
        else:
            x_1 = (-b + math.sqrt(d)) / (2 * a)
            x_2 = (-b - math.sqrt(d)) / (2 * a)
            return round(x_1, 4), round(x_2,4)


if __name__ == '__main__':
    quadratic_equation()
