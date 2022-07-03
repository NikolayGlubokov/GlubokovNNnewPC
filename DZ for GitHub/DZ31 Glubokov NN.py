from abc import ABC, abstractmethod
import os.path
import os
from math import *
from random import *
import re
import time


class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError('Секунды должны быть числом')
        self.__sec = sec % self.__DAY

    def get_format_time(self):
        s = self.__sec % 60
        m = (self.__sec // 60) % 60
        h = (self.__sec // 3600) % 24
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else '0' + str(x)

    def get_seconds(self):
        return self.__sec

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec + other.get_seconds())

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec - other.get_seconds())

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec * other.get_seconds())

    def __truediv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec / other.get_seconds())

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec // other.get_seconds())

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec % other.get_seconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec + other.get_seconds())

    def __isub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec - other.get_seconds())

    def __imul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec * other.get_seconds())

    def __itruediv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec / other.get_seconds())

    def __ifloordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec // other.get_seconds())

    def __imod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом данных Clock')
        return Clock(self.__sec % other.get_seconds())


c1 = Clock(600)
c2 = Clock(200)
c3 = c1 + c2
print(c3.get_format_time())
c3 = c1 - c2
print(c3.get_format_time())
c3 = c1 * c2
print(c3.get_format_time())
c3 = c1 // c2
print(c3.get_format_time())
c3 = c1 % c2
print(c3.get_format_time())
print('*' * 50)

c1 -= c2
print(c1.get_format_time())
c1 *= c2
print(c1.get_format_time())
c1 //= c2
print(c1.get_format_time())
c1 %= c2
print(c1.get_format_time())
print('*' * 50)