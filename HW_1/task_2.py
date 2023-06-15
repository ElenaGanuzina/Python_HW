"""
Задание 2.
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить, является ли треугольник разносторонним, равнобедренным или равносторонним.
"""


def triangle_check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("The triangle exists!")
        if a == b and a == c:
            print("The triangle is equilateral.")
        elif a == b or b == c or a == c:
            print("The triangle is isosceles.")
        else:
            print("The triangle is versatile.")
    else:
        print("The triangle does not exist.")


triangle_check(1, 2, 3)  # non-existing triangle
triangle_check(3, 4, 5)  # existing versatile triangle
triangle_check(5, 5, 4)  # existing isosceles triangle
triangle_check(10, 10, 10)  # existing equilateral triangle
