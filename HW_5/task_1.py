"""
Задача 1.
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""


def file_path_parse(absolute_path):
    components = absolute_path.split("/")
    path = "/".join(components[:-1])
    name, extension = components[-1].rsplit('.')
    return path, name, extension


string = "C:/Documents/Newsletters/Summer2018.pdf"
print(file_path_parse(string))
