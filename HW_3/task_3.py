"""
Задача 7.
Пользователь вводит строку текста.
? Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
? Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
? Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
"""


def frequency_dict():
    data = "".join(item for item in input("Enter some text: ") if item.isalpha())
    dictionary = {}

    # using .count()
    for elem in data:
        if elem not in dictionary:
            dictionary[elem] = data.count(elem)
    return dictionary

    # without .count()
    # for item in data:
    #    dictionary[item] = dictionary.get(item, 0) + 1

    # return sorted(dictionary.items())


print(frequency_dict())
