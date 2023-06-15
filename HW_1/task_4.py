"""
Задание 4.
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки.
"""

from random import randint


def guess_the_number():
    MINIMUM = 0
    MAXIMUM = 1001
    number = randint(MINIMUM, MAXIMUM)
    INITIAL_COUNT = 10
    count = 10

    while count > 0:
        count -= 1
        variant = int(input("Guess the number I've thought of. Try numbers from 0 to 1000: "))

        if variant < MINIMUM or variant > MAXIMUM:
            print("Your number is out of range. Try again. You have {count} attempts left." .format(count=count))
        elif variant < number:
            print("More. You have {count} attempts left." .format(count=count))
        elif variant > number:
            print("Less. You have {count} attempts left." .format(count=count))
        else:
            print("You guessed it! You've used {count} attempts.".format(count=INITIAL_COUNT - count))
            exit()

    else:
        print("You've used all attempts and haven't guess the number! You loose!")
        exit()


guess_the_number()