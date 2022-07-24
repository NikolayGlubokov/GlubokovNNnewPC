from math import *
from random import randint

line = '================'
print(line * 7)
print('Задание №1 - площади фигур')
print(line * 7)


def rectangle():
    a = int(input('Введите ширину прямоугольника: '))
    b = int(input('Введите высоту прямоугольника: '))
    return a * b


def triangle():
    a = int(input('Введите величину основания треугольника: '))
    b = int(input('Введите высоту треугольника: '))
    return (a * b) / 2


def circle():
    a = int(input('Введите радиус круга: '))
    return round(pi * a * a, 2)


v = int(input('Введите фигуру, площадь которой вы хотите найти (1 - прямоугольник, 2 - треугольник, 3 - круг: '))
if v == 1:
    print('Площадь прямоугольника равна:', rectangle())
elif v == 2:
    print('Площадь треугольника равна:', triangle())
else:
    print('Площадь круга равна:', circle())

print(line * 7)
print('Задание №2 - целые числа')


def spisok(x):
    lst = []
    for i in x:
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1
        if c == 2:
            lst.append(i)
    print('минимальное натуральное число списка равно: ', min(lst))
    print('минимальное натуральное число списка равно: ', max(lst))

n = int(input(' Введите длину списка: '))
matrix = [randint(0, 20) for j in range(n)]
print('Ваш список чисел: ', matrix)

spisok(matrix)
