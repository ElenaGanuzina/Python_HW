"""
Задание №2
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""

from random import randint
from random import choice

__all__ = ['sem_07_2']

MINIMUM = 4
MAXIMUM = 7
VOWELS = 'аяиыеёюяоу'
CONSONANTS = 'бвгджзйклмнпрстфхцчшщ'


def write_names(filename, row_count):
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(row_count):
            a = ""
            for i in range(randint(MINIMUM, MAXIMUM)):
                if i in (1, 3):
                    a += choice(CONSONANTS)
                else:
                    a += choice(VOWELS)

            f.write(f"{a.capitalize()}\n")


if __name__ == '__main__':
    write_names('names.txt', 5)
