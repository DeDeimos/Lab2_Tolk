from lab_python_oop.Circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
import numpy as np

if __name__ == '__main__':
    variant = 22

    r = Rectangle("красного", 2, 3)
    c = Circle("зеленного", 2)
    s = Square("синего", 3)
    print(r)
    print(c)
    print(s)

    a = np.array([1,2,3,4])
    print(a)
    print("+")
    b = np.array([5, 6, 7, 8])
    print(b)
    print("=")
    print(a+b)