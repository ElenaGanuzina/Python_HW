"""
Задача 2.
Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
"""


def key_data_dict(**kwargs):
    dictionary = {}
    for key, value in kwargs.items():
        if hash_check(value):
            dictionary.setdefault(value, key)
        else:
            dictionary.setdefault(str(value), key)
    return dictionary


def hash_check(value):
    try:
        hash(value)
    except TypeError:
        return False
    return True


print(key_data_dict(group=333, name='Sam', marks=[3, 5, 2]))