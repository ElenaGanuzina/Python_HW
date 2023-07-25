import json
from User import User
from Exceptions import AccessException, LevelException


class Project:
    def __init__(self, users: list):
        self.users = users
        self.admin = None

    @classmethod
    def load(cls, file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                users_dict = json.load(f)
        except Exception as e:
            print(f'Opening {file_name} has caused Exception {e}.')
        else:
            users = []
            for level, user in users_dict.items():
                for user_id, name in user.items():
                    users.append(User(user_id, name, level))

            return Project(users)

    def str(self):
        return f'Project has been created.'

    def log_in(self, user_id, name, level):
        user_new = User(user_id, name, level)
        if user_new not in self.users:
            raise AccessException(user_id)
        for user in self.users:
            if user_new == user:
                self.admin = user

    def add_user(self, user_id, name, level):
        if int(self.admin.level) >= int(level):
            raise LevelException(level, name)
        self.users.append(User(user_id, name, level))


if __name__ == '__main__':
    filename = 'access_code.json'
    project = Project.load(filename)
    print(project.str())
    #project.log_in('666', 'Sam', 1)
    #print(project.admin)
    #project.add_user('002', 'Ann', 7)
    #print(*project.users)
