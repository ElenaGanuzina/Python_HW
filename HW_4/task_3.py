"""
Задание №8
? Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
? Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
? Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""


def func():
    temp_dict = {}
    my_dict = {key: value for key, value in globals().items() if key.endswith('s') and key != 's'}
    for key, value in my_dict.items():
        temp_dict[str(key)[:-1]] = value
        my_dict[key] = None
    # Проверка исходных сохраненных значений.
    # print(temp_dict)
    return my_dict


s = 99
hosts = "Sam & Alex"
mem = 1000
speed = "Null"
goals = 3
sticks = 10

print(func())
