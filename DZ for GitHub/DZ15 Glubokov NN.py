from math import *
from random import *


def rhombus(**a):
    b = list(a.values()) #я использовал данный перевод, потому что возможно пользователь может ввести в функцию не те названия, которые стоят в формуле
    s = (b[0] * b[1]) / 2 # плюс ко всему, значения ставятся в таком же порядке, что и были введены в функцию.
    return s


def squared(**a):
    b = list(a.values())
    s = b[0] ** 2
    return s


def trapezoid(**a):
    b = list(a.values())
    s = ((b[0] + b[1]) * b[2]) / 2
    return s


def circle(**a):
    b = list(a.values())
    s = (b[0] ** 2) * pi
    return s


def funct(figure_type='unknown', **args):
    if figure_type == 'rhombus':
        print(rhombus(**args))
    elif figure_type == 'squared':
        print(squared(**args))
    elif figure_type == 'trapezoid':
        print(trapezoid(**args))
    elif figure_type == 'circle':
        print(circle(**args))
    else:
        print('Invalid data')


funct(figure_type='rhombus', d1=10, d2=8)
funct(figure_type='squared', a=5)
funct(figure_type='trapezoid', a=12, b=3, h=6)
funct(figure_type='circle', r=18)
funct(figure_type='unknown', a=5, b=2, c=3)

