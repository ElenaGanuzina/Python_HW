"""
Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""

from animals import Animal, Bird, Fish, Insect


class Fabric:
    classes = {"Bird": Bird, "Fish": Fish, "Insect": Insect}

    def _choose_animal(self, animal_class):
        return self.classes[animal_class]

    def create_animal(self, animal_class: str, *args, **kwargs):
        animal = self._choose_animal(animal_class)
        return animal(*args, **kwargs)


if __name__ == "__main__":
    fab = Fabric()
    anim_1 = fab.create_animal("Fish", "Crane", 2)
    print(anim_1.get_light_level())



