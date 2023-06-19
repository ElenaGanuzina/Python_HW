"""
Задача 3.
Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.
"""

MINIMUM = 50.0
MAXIMUM = 5_000_000.0
BONUS = 0.03
WEALTH_TAX = 0.1
COMMISSION = 0.015
MIN_SUM = 30.0
MAX_SUM = 600.0
BONUS_COUNT = 3
operations = []


def add_money(balance, count):
    global operations
    while True:
        total = float(input("Введите сумму, кратную 50: "))
        if total % MINIMUM == 0:
            break
        else:
            print("Некорректная сумма!")

    if balance >= MAXIMUM:
        balance -= ((balance - MAXIMUM) * WEALTH_TAX)
    if count % BONUS_COUNT == 0:
        balance += (balance * BONUS)
    balance += total
    operations.append(f'Поступление: {total}\n')
    print(f"Ваш баланс равен {balance}")
    return balance


def withdraw_money(balance, count):
    global operations
    while True:
        total = float(input("Введите сумму, кратную 50: "))
        if total > balance:
            print("Недостаточно средств на счете!")
            break
        if total % MINIMUM == 0:
            break
        else:
            print("Некорректная сумма!")

    if balance >= MAXIMUM:
        balance -= ((balance - MAXIMUM) * WEALTH_TAX)
    if balance == 0.0 or balance < total:
        return balance
    else:
        commission = total * COMMISSION
        if commission < MIN_SUM:
            commission = MIN_SUM
        elif commission > MAX_SUM:
            commission = MAX_SUM

        balance -= (total + commission)
        operations.append(f'Изъятие: {total}\n')
    if count % BONUS_COUNT == 0:
        balance += (balance * BONUS)

    print(f"Ваш баланс равен {balance}")
    return balance


def exit_program():
    print("Благодарим за пользование нашими услугами! Ждем Вас снова!")


def atc_machine():
    count = 0
    balance = 0.0

    print("Вас приветствует банкомат!")
    while True:
        action = int(input("Выберите необходимое действие: \n"
                           "1 - Пополнить счет \n"
                           "2 - Снять деньги \n"
                           "0 - Выход \n"))

        if action == 1:
            balance = add_money(balance, count)
            count += 1
        elif action == 2:
            balance = withdraw_money(balance, count)
            count += 1
        elif action == 0:
            exit_program()
            break
        else:
            print("Ошибка ввода!")


atc_machine()
print(*operations)