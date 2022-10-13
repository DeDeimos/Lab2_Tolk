from lab_python_oop.figure import Shape
from lab_python_oop.color import Color
import math

class Circle(Shape):

    def __init__(self, color, r):
        self.shape = "Круг"
        self.color = Color()
        self.color = color
        self.r = r

    def area(self):
        return math.pi*self.r**2

    def __repr__(self):
        return ('{} {} цвета, с радиусом {}'.format(self.shape, self.color, str(self.r)))