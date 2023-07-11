"""
Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    upper_limb = 2

    def __init__(self, name, wing_span):
        super().__init__(name)
        self.wing_span = wing_span

    def get_wing_len(self):
        return self.wing_span / self.upper_limb


class Fish(Animal):
    light_coefficient = 0.015

    def __init__(self, name, dwell_depth):
        super().__init__(name)
        self.dwell_depth = dwell_depth

    def get_light_level(self):
        n = 1 - self.dwell_depth * self.light_coefficient
        if n < 0:
            return 0
        return n


class Insect(Animal):
    def __init__(self, name, larva_life):
        super().__init__(name)
        self.larva_life = larva_life

    def get_left_time(self, time):
        t = self.larva_life - time
        if t < 0:
            return 0
        return t
