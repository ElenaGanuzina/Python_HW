"""
Задание 1. Решить задачи, которые не успели решить на семинаре.

Задача 6.
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif.
Откажитесь от магических чисел.
Обязательно учтите год ввода Григорианского календаря.
В коде должны быть один input и один print.
"""
import math


def leap_year_check():
    GREGORIAN_START = 1582
    DIVIDER_FOR_YEARS = 4
    DIVIDER_FOR_CENTURIES = 100
    ADDITIONAL_DIVIDER_FOR_CENTURIES = 400

    year = int(input("Enter a year in yyyy format: "))

    if year >= GREGORIAN_START:
        if year % DIVIDER_FOR_YEARS != 0:
            result = False
        elif year % DIVIDER_FOR_CENTURIES == 0 and year % ADDITIONAL_DIVIDER_FOR_CENTURIES == 0:
            result = True
        else:
            result = False
    else:
        if year % DIVIDER_FOR_YEARS != 0:
            result = False
        else:
            result = True
    print(result)


leap_year_check()

'''
Задача 7. 
Пользователь вводит число от 1 до 999. Используя операции с числами,
сообщите, что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например, 5 - 25.
Для двузначного числа - произведение цифр, например, 30 - 0.
Для трёхзначного числа - его зеркальное отображение, например, 520 - 25.
Если число не из диапазона, запросите новое число.
Откажитесь от магических чисел.
В коде должны быть один input и один print.
'''


def digit_operations():
    TEN = 10
    HUNDRED = 100
    THOUSAND = 1000
    SQUARE = 2
    result = 0
    num = 0
    while True:
        num = int(input("Enter a number from 1 to 999 inclusive: "))
        if num in range(1, THOUSAND):
            break

    if num in range(1, TEN):
        result = pow(num, SQUARE)
    elif num in range(TEN, HUNDRED):
        result = (num % TEN) * (num // TEN)
    else:
        result = num % TEN
        num //= TEN
        while num > 0:
            temp = num % TEN
            num //= TEN
            result *= TEN
            result += temp

    print(result)


digit_operations()

'''
Задача 8.
Нарисовать в консоли ёлку, спросив у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
'''


def print_christmas_tree():
    num = int(input("Enter your favourite number of rows: "))
    branch = 1
    for i in range(num):
        print((' ' * (num - i)) + ('*' * branch))
        branch += 2


print_christmas_tree()


'''
Задача 9.
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
'''


def multiplication_table():
    START = 2
    STOP = 10
    middle = (START + STOP) // 2

    for x in range(START, STOP):
        for y in range(START, middle):
            print('{0} x {1} = {2}'.format(x, y, x * y), end='\t')
        print("")

    print('\n')

    for x in range(START, STOP):
        for y in range(middle, STOP):
            print('{0} x {1} = {2}'.format(x, y, x * y), end='\t')
        print("")

multiplication_table()
