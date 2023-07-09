"""
Задание 3.

Напишите функцию, которая получает на вход директорию
и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
ля каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import os
import json
import csv
import pickle

__all__ = ['dir_data']


def find_size(path) -> int:
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        size = 0
        for item in os.scandir(path):
            if item.is_file():
                size += item.stat().st_size
            elif item.is_file():
                size += find_size(item.path)
        return size


def dir_data(string_path):
    dir_info = []
    for dir_path, dir_names, files in os.walk(string_path):
        for elem in dir_names:
            dir_info.append({"Name": elem, "Object type": "directory", "Parent": os.path.basename(dir_path),
                             "Size": find_size(f'{dir_path}/{elem}')})
        for item in files:
            dir_info.append({"Name": item, "Object type": "file", "Parent": os.path.basename(dir_path),
                             "Size": find_size(f'{dir_path}/{item}')})

    with(open("dir_info.json", "w", encoding="utf-8") as f_json,
         open("dir_info.csv", "w", newline='', encoding="utf-8") as f_csv,
         open("info.pkl", "wb") as f_pkl
         ):
        json.dump(dir_info, f_json, ensure_ascii=False, indent=2)

        writer = csv.DictWriter(f_csv, fieldnames=["Name", "Object type", "Parent", "Size"],
                                quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        writer.writerows(dir_info)

        pickle.dump(dir_info, f_pkl)

    return dir_info


if __name__ == "__main__":
    dir_ = "Enter the path to your directory."
    dir_data(dir_)

