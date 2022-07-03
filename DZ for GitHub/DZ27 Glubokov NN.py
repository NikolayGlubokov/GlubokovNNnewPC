import os.path
import os
from math import *
from random import *
import re
import time


class Pound:
    def __init__(self, x):
        if isinstance(x, int) or isinstance(x, float):
            self.__x = x
        else:
            self.__x = 1


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, int) or isinstance(x, float):
            self.__x = x
        else:
            self.__x = self.__x

    @x.deleter
    def x(self):
        del self.__x

    def get_pound(self):
       print(f'{self.__x} киллограмм ==> {round(self.__x * 2.205,2)} фунтов')


p1 = Pound(10)
print(p1.__dict__)
p1.x = '334.23'
p1.get_pound()
print(p1.__dict__)
print(p1.x)
del p1.x
print(p1.__dict__)
