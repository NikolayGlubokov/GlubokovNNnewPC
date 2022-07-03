from math import *
from specgeometry import rectangle, circle


class Cylinder(rectangle.Rectangle, circle.Circle):
    def __init__(self, a, r, b):
        rectangle.Rectangle.__init__(self, a, b)
        circle.Circle.__init__(self, r)

    def info(self):
        print(f'Радиус цилиндра: {self.r}\n'
              f'Высота цилиндра: {self.b}')

    def area(self):
        return round((pi*self.r**2)*2+2*pi*self.r*self.b,2)

    def area_circle(self):
        return round(pi*self.r**2,2)

    def value(self):
        return round(self.b*pi*self.r**2,2)

