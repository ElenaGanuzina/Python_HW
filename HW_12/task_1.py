"""
Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
"""
import csv


class GradeValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError(f'The attribute "{self.name}" cannot be deleted.')

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'The value must be an integer.')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'The value must be greater of equal {self.min_value}.')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'The value must be less {self.max_value}.')


class NameValidator:
    def __init__(self, check_1, check_2):
        self.check_1 = check_1
        self.check_2 = check_2

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        if not isinstance(value, str):
            raise TypeError(f'The value must be of string type.')
        if not self.check_1(value) or not self.check_2(value):
            raise ValueError(f'The value must consist of letters only and have its first letter capital.')
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'The attribute "{self.param_name}" cannot be deleted.')


class Student:
    mark = GradeValidator(2, 5 + 1)
    test = GradeValidator(0, 100 + 1)
    last_name = NameValidator(str.isalpha, str.istitle)
    name = NameValidator(str.isalpha, str.istitle)
    middle_name = NameValidator(str.isalpha, str.istitle)

    def __init__(self, last_name, name, middle_name, csv_file):
        self.last_name = last_name
        self.name = name
        self.middle_name = middle_name
        self.subjects = {}
        with open(csv_file, 'r', encoding='utf-8') as f:
            lines = csv.reader(f)
            for row in lines:
                subj = str(*row)
                self.subjects[subj] = {"marks": [], "tests": []}

    def __str__(self):
        return (f'{self.last_name} {self.name} {self.middle_name}'
                f'\naverage mark - {self.average_marks()}, '
                f'\naverage test results - {self.average_test()}.')

    def set_mark(self, subject: str, mark: int, mark_type: str = "subj"):
        if mark_type == "subj":
            self.mark = mark
            self.subjects[subject]["marks"].append(self.mark)
        if mark_type == "test":
            self.test = mark
            self.subjects[subject]["tests"].append(self.test)

    def average_test(self):
        test_results = {}
        for key, value in self.subjects.items():
            test_sum = 0
            for item in value['tests']:
                test_sum += item
                test_results[key] = round(test_sum / len(value['tests']), 4)
        return test_results

    def average_marks(self):
        average_marks = {}
        for key, value in self.subjects.items():
            marks_sum = 0
            for item in value['marks']:
                marks_sum += item
                average_marks[key] = marks_sum / len(value['marks'])
        return average_marks


if __name__ == '__main__':
    student = Student("Smith", "Alex", "Daniel", 'subjects.csv')
    # student_1 = Student("sdfasd", "12", "sldk", 'subjects.csv')
    student.set_mark("Maths", 5)
    student.set_mark("Maths", 67, "test")
    student.set_mark("Maths", 4)
    student.set_mark("Maths", 76, "test")
    student.set_mark("Physics", 3)
    student.set_mark("Physics", 33, "test")
    student.set_mark("Physics", 4)
    student.set_mark("Physics", 56, "test")
    student.set_mark("English", 5)
    student.set_mark("English", 94, "test")
    student.set_mark("English", 5)
    student.set_mark("English", 89, "test")
    # student.set_mark("PE", 1001, "test")
    # student.set_mark("PE", 7)
    print(student.subjects)
    print(student.average_marks())
    print(student.average_test())
