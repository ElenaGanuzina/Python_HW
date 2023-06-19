"""
Задание №7
? Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
? Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""


def profit_check(some_dict):
    lst = []
    for value in some_dict.values():
        lst.append(sum(value))
        print(lst)
    if all(item > 0 for item in lst):
        return True
    else:
        return False


companies_dict = {"Oceanic Airlines": [900, -460, 843, -735, 333],
                  "Cyberdyne Systems": [666, -342, 392, 234, 574, -711],
                  "RDA": [-596, -372, 498, 459],
                  "U. S. Robots": [333, 444, 555, 666, 777, 111, -222]}

print(profit_check(companies_dict))