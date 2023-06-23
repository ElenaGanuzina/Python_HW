"""
Задача 7 + задача 2 из д/з.
Создайте модуль и напишите в нём функцию, которая получает на вход дату в виде строки вида DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

from sys import argv

__all__ = ['date_check']

_SHORT_MONTHS = (4, 6, 9, 11)


def date_check(text: str) -> bool:
    """Checking if the date exists."""
    day, month, year = map(int, text.split("."))
    if 1 > year > 9999 or 1 > month > 12 or 1 > day > 31:
        return False
    if month in _SHORT_MONTHS and day > 30:
        return False
    if month == 2 and _leap_year_check(year) and day > 29:
        return False
    if month == 2 and not (_leap_year_check(year)) and day > 28:
        return False
    return True


def _leap_year_check(year: int) -> bool:
    """Checking if the year is leap."""
    return year % 4 == 0 or year % 100 != 0 and year % 400 == 0


if __name__ == '__main__':
    # print(date_check("31.06.1968"))
    _, date = argv
    print(date_check(date))
