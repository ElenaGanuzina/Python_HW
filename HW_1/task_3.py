"""
Задание 3.
Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""


def simple_number_check():
    MAXIMUM = 100000
    MINIMAL_COMPOSITE_NUMBER_DIVIDER = 2
    count = 0

    while True:
        num = int(input("Enter a number from 0 to 100000 inclusive: "))
        if 0 < num <= MAXIMUM:
            break
        else:
            print("Invalid input!")

    if num == 1:
        print("The number 1 is neither complex nor simple.")
        exit()

    for item in range(MINIMAL_COMPOSITE_NUMBER_DIVIDER, num // MINIMAL_COMPOSITE_NUMBER_DIVIDER + 1):
        if num % item == 0:
            count += 1

    if count == 0:
        print("The number is simple.")
    else:
        print("The number is composite.")


simple_number_check()