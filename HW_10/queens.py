"""
Возьмите любую из задач с прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства.
Задачи должны решаться через вызов методов экземпляра.
"""
from random import randint


class Queen:
    desk_size = 0
    row = []
    col = []
    coord_list = []

    def __init__(self, desk_size):
        self.desk_size = desk_size

    def queen_check(self, coord_list: list) -> bool:
        """Checking if queens beat each other"""
        for item in coord_list:
            self.row.append(item[0])
            self.col.append(item[1])
        for i in range(self.desk_size):
            for j in range(i + 1, self.desk_size):
                if self.row[i] == self.row[j] or self.col[i] == self.col[j] or \
                        abs(self.row[i] - self.row[j]) == abs(self.col[i] - self.col[j]):
                    return False
        return True

    def coordinates_gen(self, coord_list) -> list:
        """Generating a list of eight pairs of coordinates for queens."""
        for _ in range(self.desk_size):
            x, y = randint(1, self.desk_size), randint(1, self.desk_size)
            coord_list.append((x, y))
        return coord_list

    def find_solutions(self, solutions_number):
        """Finding the required number of solutions (4)."""
        count = 0
        variants = 0
        while count < solutions_number:
            coord_list = self.coordinates_gen(self.coord_list)
            variants += 1
            if self.queen_check(coord_list):
                print(*coord_list)
                print(variants)
                count += 1


if __name__ == '__main__':
    queen = Queen(8)
    print(type(queen))
    queen.find_solutions(1)
