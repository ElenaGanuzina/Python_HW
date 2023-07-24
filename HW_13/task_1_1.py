from random import randint
from sys import argv

MAXIMUM = 100
MINIMUM = 0
ATTEMPTS = 10


def guess_the_number(MINIMUM, MAXIMUM, count=ATTEMPTS):
    number = randint(MINIMUM, MAXIMUM)
    while count > 0:
        count -= 1

        try:
            variant = int(input(f"Guess the number I've thought of. Try numbers from {MINIMUM} to {MAXIMUM}: "))
        except ValueError as e:
            print(f'Your input was not an integer and has caused ValueError: {e}.')
        else:
            if MINIMUM > variant or MAXIMUM < variant:
                print(f'Your number is out of range. You have {count} attempts left.')
            elif variant < number:
                print(f'More. You have {count} attempts left.')
            elif variant > number:
                print(f'Less. You have {count} attempts left.')
            else:
                return True
            if count == ATTEMPTS:
                return False
    else:
        return False


if __name__ == '__main__':
    print(guess_the_number(0, 100))

