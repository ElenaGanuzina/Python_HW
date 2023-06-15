"""
Задание 4
? Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
? *Верните все возможные варианты комплектации рюкзака.
"""

things = {'matches': 0.05, 'compass': 0.1, 'flashlight': 0.5, 'food': 3.5,
          'axe': 2, 'aid kit': 0.5, 'kettle': 1, 'knife': 0.3, 'water bottle': 3.85,
          'sunglasses': 0.1, 'tent': 5.6, 'sleeping bag': 2.15, 'toothbrash': 0.02, 'spoon': 0.1,
          'bowl': 0.5, 'mug': 0.3, 'jacket': 0.7, 'wool socks': 0.2, 'sweater': 0.5}


def backpack(dictionary):
    weight = float(input("Enter your backpack weight capacity in kilos: "))
    lst = []
    total_weight = 0
    for k, v in things.items():
        if v <= weight:
            weight -= v
            total_weight += v
            lst.append(k)
    return lst, total_weight


print(*backpack(things), sep=", ")
