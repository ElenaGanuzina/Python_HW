"""
Задание 2.
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


def convert_to_hex(int_num):
    BASE = 16
    dictionary = '0123456789abcdef'
    result = ''

    while int_num:
        result = dictionary[int_num % BASE] + result
        int_num //= BASE

    return result


print(convert_to_hex(5))
print(hex(5))

print(convert_to_hex(16))
print(hex(16))

print(convert_to_hex(57))
print(hex(57))

print(convert_to_hex(1495))
print(hex(1495))
