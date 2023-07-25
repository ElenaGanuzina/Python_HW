"""
На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.
"""

import pytest
from Project import Project as p
from User import User


@pytest.fixture
def create_project():
    return p.load("access_code.json")


def test_create_project(create_project):
    assert create_project.str() == 'Project has been created.', "Project has not been created."


def test_admin(create_project):
    create_project.log_in("666", "Sam", 1)
    assert create_project.admin == User("666", "Sam", 1), "Admin was not assigned or the data was incorrect."


def test_add_user(create_project):
    create_project.log_in("666", "Sam", 1)
    create_project.add_user("333", "Mary", 7)
    assert create_project.users[len(create_project.users) - 1] == User("333", "Mary", 5), \
        "Could not add a new user to the project"


if __name__ == '__main__':
    pytest.main(['-v'])
