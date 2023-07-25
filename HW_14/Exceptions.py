
class BasicException(Exception):
    pass


class LevelException(BasicException):
    def __init__(self, level, name):
        self.level = level
        self.name = name

    def __str__(self):
        return f'The level {self.level} is incorrect for the user {self.name}.'


class AccessException(BasicException):
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f'Access denied fo the user {self.user_id}.'
