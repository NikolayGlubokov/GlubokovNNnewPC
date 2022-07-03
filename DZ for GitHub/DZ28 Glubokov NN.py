import os.path
import os
from math import *
from random import *
import re
import time


class Area:
    count=0
    @staticmethod
    def geron_triangle(a, b, c):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
            if (a + b) > c and (a + c) > b and (b + c) > a:
                Area.count += 1
                p = (a + b + c) / 2
                s = sqrt(p*(p - a)*(p - b)*(p - c))
                print(f'Площадь треугольника по формуле Герона равна {s}')
            else:
                print('У вас что угодно, но не треугольник')
        else:
            print('Введите нормальные данные')

    @staticmethod
    def two_indicators_triangle(h, a):
        if isinstance(a, (int, float)) and isinstance(h, (int, float)):
            Area.count += 1
            print(f'Площадь треугольника при известных величине высоты треугольника и катета,'
                  f'на который она падает, равна {a*h/2}')
        else:
            print('Введите нормальные данные')

    @staticmethod
    def square(a):
        if isinstance(a, (int, float)):
            Area.count += 1
            print(f'Площадь квадрата равна {a**2}')
        else:
            print('Введите нормальное значение')

    @staticmethod
    def rectangle(a,b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            Area.count += 1
            print(f'Площадь прямоугольника равна {a*b}')
        else:
            print('Введите нормальные значения')

    def get_count(self):
        print(f'Количество подсчетов площадей фигур равно {Area.count}')

a1 = Area()
a1.geron_triangle(3,4,17)
a1.two_indicators_triangle(10,4)
a1.square(6)
a1.rectangle(45,23)
a1.get_count()

