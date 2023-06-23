""""
Задача 4-6.
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными верными вариантами отгадок и количество попыток на угадывание.
Функция возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, из предыдущей задачи, чтобы передать ей все свои загадки.

Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.
"""

__all__ = ['guess_the_riddle', 'show_history']


ATTEMPTS = 5


def guess_the_riddle(riddle: str, lst: list) -> int:
    """Trying to guess the riddle and counting attempts"""
    print(f'Guess the riddle: {riddle}')
    for i in range(1, ATTEMPTS + 1):
        variant = input(f'Your variant: ')
        if variant in lst:
            print(f'You guessed it! You have used {i} attempts.')
            return i
        else:
            print('Wrong! Try again.')
            i += 1

    print("You've used all attempts and haven't guess the riddle! You loose!")
    return 0


def riddle_dict():
    """Storing riddles and right answer variants."""
    riddles = {'Сто одежек и все без застежек.': ['капуста', 'Капуста', 'КАПУСТА'],
               'Зимой и летом одним цветом.': ['ель', 'елка', 'ёлка', 'Елка'],
               'Шел долговяз, в сыру землю увяз.': ['дождь', 'Дождь', 'ДОЖДЬ', 'дождик']}
    for key, value in riddles.items():
        riddle_history(key, guess_the_riddle(key, value))


def riddle_history(riddle: str, attempts: int):
    """Storing the riddle and attempts made to guess it."""
    _history[riddle] = attempts


def show_history():
    """Showing the riddle and the attempts made to guess it."""
    print('\n'.join(f'You guessed the riddle {key} in {value} attempts.' for key, value in _history.items()))


_history = {}

if __name__ == '__main__':
    # _, text, lst, attempts = argv
    # print(guess_the_riddle(text, lst, ATTEMPTS))
    riddle_dict()
    show_history()
