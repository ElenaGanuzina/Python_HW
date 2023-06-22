"""
Задача 2.
Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии.
"""


def bonus_calc(names, salaries, rates):
    yield {name: (salary / 100) * float(rate.strip("%")) for name, salary, rate in zip(names, salaries, rates)}


names = ["Sam", "Dave", "Pam", "Liam"]
salaries = [230, 184, 155, 106]
rates = ["9.5%", "8.75%", "8.5%", "7.11%"]

print(*bonus_calc(names, salaries, rates))

