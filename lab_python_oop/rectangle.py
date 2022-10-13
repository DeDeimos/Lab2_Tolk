from lab_python_oop.figure import Shape
from lab_python_oop.color import Color


class Rectangle(Shape):
    def __init__(self, color, a, b):
        self.shape = "Прямоугольник"
        self.color = Color()
        self.color = color
        self.a = a
        self.b = b
    def area(self):
        return self.a*self.b

    def __repr__(self):
        return ('{} {} цвета, с шириной {} и высотой {}'.format(self.shape, self.color, str(self.a), str(self.b)))
