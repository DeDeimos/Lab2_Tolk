from lab_python_oop.rectangle import Rectangle
from lab_python_oop.color import Color


class Square(Rectangle):

    def __init__(self, color, a):
        super().__init__(color, a, a)
        self.shape = "Квадрат"

    def area(self):
        return self.a**2

    def __repr__(self):
        return ('{} {} цвета, со стороной {}'.format(self.shape, self.color, str(self.a)))