"""
Задача 3-4 из д/з.
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
для случайной расстановки ферзей в задаче выше.
Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
*Выведите все успешные варианты расстановок.
"""

from random import randint

__all__ = ['find_solutions']


def queen_check(coordinates_list: list) -> bool:
    """Checking if queens beat each other"""
    n = 8
    row = []
    col = []

    for item in coordinates_list:
        row.append(item[0])
        col.append(item[1])

    for i in range(n):
        for j in range(i + 1, n):
            if row[i] == row[j] or col[i] == col[j] or abs(row[i] - row[j]) == abs(col[i] - col[j]):
                return False
    return True


def coordinates_gen() -> list:
    """Generating a list of eight pairs of coordinates for queens."""
    number = 8
    coord_list = []
    for _ in range(number):
        x, y = randint(1, number), randint(1, number)
        coord_list.append((x, y))
    return coord_list


def find_solutions():
    """Finding the required number of solutions (4)."""
    count = 0
    variants = 0
    while count < 4:
        lst = coordinates_gen()
        variants += 1
        if queen_check(lst):
            print(*lst)
            print(variants)
            count += 1


if __name__ == '__main__':
    find_solutions()
