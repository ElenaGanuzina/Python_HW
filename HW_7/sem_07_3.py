"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""
import typing

__all__ = ['sem_07_3']


def read_per_line(file_obj: typing.TextIO):
    line = file_obj.readline()
    if line == '':
        file_obj.seek(0)
        line = file_obj.readline()
    return line[:-1]


def read_files(numbers, names, result):
    with(
        open(numbers, 'r', encoding='utf-8') as f_nums,
        open(names, 'r', encoding='utf-8') as f_names,
        open(result, 'w', encoding='utf-8') as f_res
    ):
        len_names = sum(True for _ in f_names)
        len_nums = sum(1 for _ in f_nums)
        for _ in range(max(len_names, len_nums)):
            name = read_per_line(f_names)
            num = read_per_line(f_nums)
            int_num, float_num = num.split('|')
            int_num, float_num = int(int_num), float(float_num)
            mult = int_num * float_num
            if mult > 0:
                f_res.write(f'{name.upper()}|{round(mult)}\n')
            else:
                f_res.write(f'{name.lower()}|{abs(mult)}\n')


if __name__ == '__main__':
    read_files('numbers.txt', 'names.txt', 'result.txt')
