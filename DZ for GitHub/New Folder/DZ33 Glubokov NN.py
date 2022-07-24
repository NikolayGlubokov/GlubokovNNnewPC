import os.path
import os
from math import *
from random import *
import re
import time

class NonNegative:
     def __set_name__(self, owner, name):
         self.__name = name

     def __get__(self, instance, owner):
         return instance.__dict__[self.__name]

     def __set__(self, instance, value):
         if value < 0:
             raise ValueError(f"Значение должно быть положительным")
         instance.__dict__[self.__name] = value

class Rectangle:
     a = NonNegative()
     b = NonNegative()
     c = NonNegative()

     def __init__(self, a, b, c):
         self.a=a
         self.b=b
         self.c=c


     def triangle_info(self):
         if ((self.a+self.b)>self.c) and ((self.b+self.c)>self.a) and ((self.a+self.c)>self.b):
             print(f'Данный треугольник со сторонами {self.a}, {self.b}, {self.c}  существует.')
         else:
             print(f'Данный треугольник со сторонами {self.a}, {self.b}, {self.c}  не существует.')

r1=Rectangle(3,5,7)
r1.triangle_info()