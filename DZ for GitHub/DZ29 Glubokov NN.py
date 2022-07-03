import os.path
import os
from math import *
from random import *
import re
import time

class Figure:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    def product_of_numbers(self):
        print(f'Произведение катетов равно: {self.__a * self.__b}')

    def sum_of_numbers(self):
        print(f'Сумма катетов равна:{self.__a + self.__b}')


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__(a, b)

    def gipp(self):
        return ((self.a ** 2) + (self.b ** 2)) ** 0.5

    def area(self):
        return (self.a * self.b / 2)

    def rectangle_info(self):
        print(f'Мы имеем треугольник с сторонами {self.a}, {self.b}, {round(self.gipp(), 2)}')
        print(f'Гипотенуза треугольника АВС равна:', round(self.gipp(), 2))
        print(f'Площадь треугольника равна:', round(self.area(), 2))
        self.sum_of_numbers()
        self.product_of_numbers()


rect = Rectangle(10, 20)
print(rect.gipp())
print(rect.area())
rect.a = 13
print(rect.gipp())
print(rect.area())
rect.sum_of_numbers()
rect.rectangle_info()