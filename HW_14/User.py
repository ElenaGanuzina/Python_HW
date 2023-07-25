import csv
import json


class User:
    def __init__(self, user_id, name, level):
        self.user_id = user_id
        self.name = name
        self.level = level

    def __str__(self):
        return f'User.\t Id: {self.user_id},\t name: {self.name},\t access level: {self.level}\n'

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name


def add_user_to_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            my_dict = json.load(f)

    except Exception:
        my_dict = {str(level): {} for level in range(1, 8)}
    print(f'{my_dict = }')
    while True:
        name, user_id, level, *_ = input("Enter name, id, and access level using space: ").split()
        try:
            if user_id not in my_dict[level].keys():
                my_dict[level].update({user_id: name})
                break
            else:
                print('Id is not unique')
        except KeyError as e:
            print(f'KeyError {e}')
    print(f'{my_dict = }')
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_dict, f, indent=1, ensure_ascii=False)


if __name__ == '__main__':
    add_user_to_file("access_code.json")
    user_1 = User("1", "Sam", "1")
    user_2 = User("2", "Sam", "1")
    print(user_1 == user_2)





