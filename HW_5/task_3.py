"""
Задача 3.
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""
from time import sleep


def fibonacci_gen():
    x, y= 0, 1
    while True:
        yield x + y
        sleep(2)
        y = x + y
        x = y - x


def print_fib(num):
    for num in fibonacci_gen():
        print(f'{num}\n')


print_fib(fibonacci_gen())
