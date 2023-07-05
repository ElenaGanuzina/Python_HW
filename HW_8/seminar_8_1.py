"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""

import json

__all__ = ['new_json_file']


def new_json_file(file_name: str):
    data = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            key, value = line.replace('\n', '').split('|')
        data[key.capitalize()] = value

    with open('new_file.json', 'w', encoding='utf-8') as jf:
        json.dump(data, jf, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    new_json_file('result.txt')
