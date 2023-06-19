"""
Задание 2

Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов.
"""

lst = [10, 4, 5, 33, 33, 7, 0, 3, 7, 9, 0]


def frequent_elements(my_lst):
    new_lst = []
    for item in set(my_lst):
        if my_lst.count(item) > 1:
            new_lst.append(item)
    return new_lst


print(frequent_elements(lst))
