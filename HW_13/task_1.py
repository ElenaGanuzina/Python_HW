class Rectangle:
    """Test class Rectangle."""
    __slots__ = ('_length', '_width')

    def __init__(self, length, width=None):
        """Creates a rectangle."""
        self._length = length
        if width is None:
            self._width = length
        else:
            self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError(f"Rectangular length cannot be negative.")
        else:
            self._length = value

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError(f"Rectangular width cannot be negative.")
        else:
            self._width = value

    def __str__(self):
        return f'Rectangle with length = {self.length} and width = {self.width}.'

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width}'

    def get_perimeter(self):
        """Finds perimeter of a rectangle."""
        return 2 * (self.length + self.width)

    def get_area(self):
        """Finds area of a rectangle."""
        return self.width * self.length

    def __add__(self, other):
        """Creates a new rectangle with a perimeter equal to the sum of the perimeters of the two given rectangles."""
        p = self.get_perimeter() + other.get_perimeter()
        a = p * 0.6
        b = p * 0.4
        return Rectangle(a, b)

    def __sub__(self, other):
        """Creates a new rectangle with a perimeter equal to the difference of the perimeters of the two given
        rectangles."""
        p = abs(self.get_perimeter() - other.get_perimeter())
        a = p * 0.6
        b = p * 0.4
        return Rectangle(a, b)

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()


if __name__ == '__main__':
    rec_1 = Rectangle(4, 5)
    rec_2 = Rectangle(7, 4)
    print(f'{rec_1.get_perimeter() = }\n{rec_2.get_perimeter() = }')
    rec_3 = rec_1 - rec_2
    rec_4 = rec_1 + rec_2
    print(f'{rec_3.get_perimeter() = }\n{rec_4.get_perimeter() = }')
    print(rec_4 == rec_1)
    print(rec_4 != rec_1)
    print(rec_4 > rec_1)
    print(rec_4 < rec_1)
    print(rec_4 <= rec_1)
    print(rec_4 >= rec_1)