"""
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""
import csv
import json

__all__ = ['create_csv']


def create_csv(file_name, csv_file):
    with (open(file_name, 'r', encoding='utf-8') as f,
          open(csv_file, 'w', newline='', encoding='utf-8') as f_c):

        json_dict = json.load(f)
        rows = []
        for level, other in json_dict.items():
            for user_id, name in other.items():
                rows.append({'id': user_id, 'level': int(level), 'name': name})
        res = csv.DictWriter(f_c, fieldnames=["id", "level", "name"])
        res.writeheader()
        res.writerows(rows)


if __name__ == '__main__':
    create_csv("seminar_8/access_code.json", "access.csv")
