"""
Задача 5.
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""

lst = [2, 5, 4, 3, 2, 4, 6, 5, 3]


def odd_number_index(my_lst):
    new_lst = []
    for i, item in enumerate(my_lst, 1):
        if item % 2 != 0:
            new_lst.append(i)
    return new_lst


print(odd_number_index(lst))
