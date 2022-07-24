from math import *
from random import *

liner = '---------------'
print(liner * 7)
print('Задание №1 - Двойная функция')


def func1(x):
    def func2(y):
        s = x * y
        return s

    return func2


res = func1(3)
print(res(20))
print(res(15))
res = func1(10)
print(res(15))
print(res(15))

print(liner * 7)
print('Задание №2 - Лямбда-функция: множение трёх чисел')
print((lambda x, y, z: x * y * z)(5, 5, 4))
print(liner * 7)
print('Задание №3 - Сортировка списка со словарями')
lst = [{'name': 'Jennifer', 'final': 95}, {'name': 'David', 'final': 92}, {'name': 'Nikolas', 'final': 98}]
y = sorted(list(lst[i]['name'] for i in range(len(lst))))
z = sorted(list(lst[i]['final'] for i in range(len(lst))))


def srtd(x):
    lst2 = []
    lst3 = []
    minim = min(z)
    maxim = max(z)

    def name_sort():
        for i in y:
            for j in x:
                if j['name'] == i:
                    lst2.append(j)
        print(lst2)

    def result_sort():
        for i in reversed(z):
            for j in x:
                if j['final'] == i:
                    lst3.append(j)
        print(lst3)

    def mn():
        for i in x:
            if i['final'] == minim:
                return i

    def mx():
        for i in x:
            if i['final'] == maxim:
                return i

    def replace():
        pass

    replace.ns = name_sort
    replace.rs = result_sort
    replace.mn = mn
    replace.mx = mx
    return replace


solve = srtd(lst)

print(solve.ns())
print(solve.rs())
print(liner * 7)
print('Задание №4 - Выведение максимального и минимального баллов')
print(solve.mn())
print(solve.mx())

