class BasicException(ValueError):
    pass


class NegativeValueException(BasicException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Rectangular side cannot have negative value: {self.value}.'


class NotIntegerException(BasicException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'The value {self.value} is not of integer type.'
