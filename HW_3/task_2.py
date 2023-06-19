"""
Задача 6.
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
? Строки нумеруются начиная с единицы.
? Слова выводятся отсортированными согласно кодировки Unicode.
? Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""


def sorted_words():
    SPACE = 1
    data = input("Enter something: ")
    lst = data.split()
    lst.sort()
    maxi = len(max(lst, key=len))
    maxi = maxi + SPACE
    for i, elem in enumerate(lst, 1):
        print(f'{i}{elem:>{maxi}}')


sorted_words()
