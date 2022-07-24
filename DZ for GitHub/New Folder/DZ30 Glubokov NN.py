from abc import ABC, abstractmethod
import os.path
import os
from math import *
from random import *
import re
import time


class Root(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def root(self):
        pass

    def print_value(self):
        print(self.value, end=' ')


class LinearRoot(Root):

    def root(self):
        b = re.findall(r'[+-]?[0-9]+', self.value)
        if self.value.index('x') < self.value.index(b[1]):
            pass
        else:
            b[0], b[1] = b[1], b[0]
        for i in range(len(b)):
            b[i] = int(b[i])
        return b[1] / b[0]

    def print_value(self):
        print(f'The root of {self.value} is: {self.root()}')


#
class QuatroRoot(Root):

    def transformation(self):
        c = self.value
        c = re.sub(r'[\^]2', '', c)
        c = re.sub(r'[\*\*]2', '', c)
        c = re.sub(r'[a-z]2', '', c)
        b = re.findall(r'[+-]?[0-9]+', c)
        for i in range(len(b)):
            b[i] = int(b[i])
        return b

    def root(self):
        s = self.transformation()
        lst = []
        d = s[1] ** 2 - 4 * s[0] * s[2]
        if d > 0:
            lst.append(((-s[1] + d ** 0.5) / (2 * s[0])))
            lst.append(((-s[1] - d ** 0.5) / (2 * s[0])))
        elif d == 0:
            lst.append(((-s[1]) / (2 * s[0])))
        else:
            lst.append("not")
        return lst

    def print_value(self):
        print(f'The roots of {self.value} are: x1={self.root()[0]}, x2={self.root()[1]}')


p1 = LinearRoot('9x+18=0')
p1.print_value()
p2 = QuatroRoot('1x^2-2x-3=0')

p2.print_value()
