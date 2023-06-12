"""
Задание 3.
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
"""
import fractions
from math import gcd


def using_fractions(f_1: str, f_2: str):
    nom1, den1 = map(int, f_1.split("/"))
    nom2, den2 = map(int, f_2.split("/"))

    if den1 == 0 or den2 == 0:
        return print("Division by zero is forbidden!")

    else:
        nom, den = multiplication(nom1, nom2, den1, den2)
        nom_add, den_add = addition(nom1, nom2, den1, den2)

    print(f'Result of multiplication: {nom}/{den}')
    print(f'Result of addition: {nom_add}/{den_add}')


def multiplication(nom1, nom2, den1, den2):
    nom = nom1 * nom2
    den = den1 * den2
    com_div = gcd(nom, den)
    nom //= com_div
    den //= com_div
    return nom, den


def addition(nom1, nom2, den1, den2):
    if den1 == den2:
        nom_add = (nom1 + nom2)
        nom = nom_add // gcd(nom_add, den1)
        return nom, den1
    else:
        com_div = int(gcd(den1, den2))
        den = int((den1 * den2) / com_div)
        add_mult1 = int(den2 / com_div)
        add_mult2 = int(den1 / com_div)
        nom = (nom1 * add_mult1) + (nom2 * add_mult2)
        nom = nom // gcd(nom, den)
        den = den // gcd(nom, den)
        return nom, den


def checking_result(nom1, den1, nom2, den2):
    a = fractions.Fraction(nom1, den1)
    b = fractions.Fraction(nom2, den2)
    print(f'Checking result: {a * b}, {a + b}')
    print()


using_fractions("3/8", "6/11")
checking_result(3, 8, 6, 11)

using_fractions("3/4", "3/0")
print()

using_fractions("17/121", "5/13")
checking_result(17, 121, 5, 13)

using_fractions("5/23", "8/23")
checking_result(5, 23, 8, 23)
