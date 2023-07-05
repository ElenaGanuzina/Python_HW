"""
Задание 1.

Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из предыдущей задачи.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""
import csv
import pickle

__all__ = ['pickle_to_csv']


def pickle_to_csv(file):
    csv_file = file.split(".")[0] + ".csv"
    with (open(file, "rb") as f,
          open(csv_file, "w", newline='', encoding='utf-8') as csv_f
          ):
        dict_list = pickle.load(f)
        print(dict_list)
        headers = [item for item in dict_list[0].keys()]
        csv_writer = csv.DictWriter(csv_f, fieldnames=headers, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        for elem in dict_list:
            csv_writer.writerow(elem)


if __name__ == "__main__":
    pickle_to_csv('user.pkl')
