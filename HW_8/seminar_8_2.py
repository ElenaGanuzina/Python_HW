"""
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""

import json
import os

__all__ = ['access_code']


def access_code(file_json):
    if os.path.isfile(file_json):
        with open(file_json, 'r', encoding='utf-8') as f:
            my_dict = json.load(f)
    else:
        my_dict = {str(i): {} for i in range(1, 8)}

    while True:
        data = input("Enter your name, id and access using space: ")
        if not data:
            break
        name, user_id, access = data.split()
        if user_id not in my_dict[access]:  # and my_dict[access][user_id] == name:
            my_dict.setdefault(access, {user_id: name})[user_id] = name

    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(my_dict, f, ensure_ascii=False)


if __name__ == '__main__':
    access_code("seminar_8/access_code.json")
