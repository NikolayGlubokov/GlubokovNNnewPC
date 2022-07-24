from abc import ABC, abstractmethod
import os.path
import os
from math import *
from random import *
import re
import time


class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # @property
    # def x(self):
    #     return self.__x
    #
    # @x.setter
    # def x(self, value):
    #     self.__x = value
    #
    # @property
    # def y(self):
    #     return self.__y
    #
    # @y.setter
    # def y(self, value):
    #     self.__y = value
    #
    # @property
    # def z(self):
    #     return self.__z
    #
    # @z.setter
    # def z(self, value):
    #     self.__z = value

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError('Key is not str')
        if item == 'x':
            return self.x
        if item == 'y':
            return self.y
        if item == 'z':
            return self.z

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Key is not str')
        if not isinstance(value, int):
            raise ValueError('Value is not int')

        if key == 'x':
            self.x = value
        elif key == 'y':
            self.y = value
        elif key == 'z':
            self.z = value

    def all_coords(self):
        return (self.x, self.y, self.z)

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)


p1 = Point3D(3, 5, 7)
print(p1.all_coords())
print(p1['x'], p1['y'], p1['z'])
p2 = Point3D(1, 2, 3)
print(p2['x'], p2['y'], p2['z'])
p3 = p1 + p2
print(p3['x'], p3['y'], p3['z'])
p3['x'] = 14
print(p3['x'], p3['y'], p3['z'])
p4 = p1 - p2
print(p4['x'], p4['y'], p4['z'])
p5 = p1 * p2
print(p5['x'], p5['y'], p5['z'])
p6 = p5 / p2
print(p6['x'], p6['y'], p6['z'])

s = 1
for i in p1, p2:
    print(f"x{s}:{i['x']}", end='    ')
    s += 1
print()
s = 1
for i in p1, p2:
    print(f"y{s}:{i['y']}", end='    ')
    s += 1
print()
s = 1
for i in p1, p2:
    print(f"z{s}:{i['z']}", end='    ')
    s += 1
print()
