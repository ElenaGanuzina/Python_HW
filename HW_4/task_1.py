"""
Задача 6.
? Функция получает на вход список чисел и два индекса.
? Вернуть сумму чисел между между переданными индексами.
? Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""


def sum_list_num(some_list, start, end):
    if start < 0:
        start = 0
    if end > len(some_list):
        end = len(lst) + 1
    result = 0
    for elem in some_list[start:end]:
        result += elem
    return result


lst = [4, 6, 9, 10, 1]
print(sum_list_num(lst, 0, 5))
