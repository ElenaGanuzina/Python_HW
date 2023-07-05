"""
Задание 2.

Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
"""
import csv
import pickle

__all__ = ['read_csv_file']


def read_csv_file(csv_file):
    with open(csv_file, "r", newline='', encoding="utf-8") as f:
        reader = [*csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)]
        data = {}
        for line in reader[1:]:
            for elem, item in zip(reader[0], line):
                data[elem] = item
            print(data)
            print(pickle.dumps(data))


if __name__ == "__main__":
    read_csv_file("user.csv")