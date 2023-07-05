"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""
import csv
import json

__all__ = ['processing_csv_file']


def processing_csv_file(csv_file, json_file):
    with (open(csv_file, 'r', newline='', encoding='utf-8') as f,
          open(json_file, 'w', encoding='utf-8') as jf):
        lines = [*csv.reader(f)]
        h_id, h_acc, h_name = lines[0]
        lst = []
        for user_id, access, name in lines[1:]:
            lst.append({h_id: user_id, h_acc: access, h_name: name, 'hash': hash(user_id + name)})
        json.dump(lst, jf, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    processing_csv_file('seminar_8/access.csv', 'users.json')
