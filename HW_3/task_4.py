"""
Задача 8.
Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
? Какие вещи взяли все три друга
? Какие вещи уникальны, есть только у одного друга
? Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
? Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""

friends = {'Dan': ('tent', 'sleeping bag', 'matches', 'knife', 'guitar'),
           'Mike': ('sleeping bag', 'kettle', 'knife', 'flashlight', 'axe'),
           'Sam': ('sleeping bag', 'knife', 'matches', 'flashlight')}


def common_staff(dictionary):
    """Какие вещи взяли все три друга."""
    temp = []
    for value in dictionary.values():
        for item in value:
            temp.append(item)
    return {element for element in temp if temp.count(element) == len(dictionary)}


def unique_staff(dictionary):
    """Какие вещи уникальны, есть только у одного друга."""
    temp = []
    for value in dictionary.values():
        for item in value:
            temp.append(item)
    return [element for element in temp if temp.count(element) == 1]


print(*common_staff(friends), sep=", ")
print(*unique_staff(friends), sep=", ")
