"""
Задание 2.
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


def convert_to_hex(int_num):
    BASE = 16
    dictionary = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                  6: '6', 7: '7', 8: '8', 9: '9', 10: 'a',
                  11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    result = ''

    while int_num > 0:
        result = dictionary.get(int_num % BASE) + result
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
