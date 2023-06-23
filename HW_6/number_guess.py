"""
Задача 2-3.
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

Улучшаем задачу 1.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
"""

from random import randint
from sys import argv

__all__ = ['guess_the_number']

MAXIMUM = 100
MINIMUM = 0
ATTEMPTS = 10


def guess_the_number(MINIMUM, MAXIMUM, count=ATTEMPTS):
    number = randint(MINIMUM, MAXIMUM)
    while count > 0:
        count -= 1
        variant = int(input(f"Guess the number I've thought of. Try numbers from {MINIMUM} to {MAXIMUM}: "))
        if MAXIMUM < variant < MINIMUM:
            print(f'Your number is out of range. Try again. You have {count} attempts left.')
        elif variant < number:
            print(f'More. You have {count} attempts left.')
        elif variant > number:
            print(f'Less. You have {count} attempts left.')
        else:
            return True
        if count == ATTEMPTS:
            return False

    else:
        return False


# print(guess_the_number(MINIMUM, MAXIMUM, ATTEMPTS))


if __name__ == '__main__':
    _, *params = argv
    print(guess_the_number(*map(int, params)))

# Запуск функции из модуля в терминале
# cd HW_6
# python task_1.py 0 100 10
