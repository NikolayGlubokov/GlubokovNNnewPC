from math import *
from random import *
import re
import time

liner = '---------------'
print(liner * 7)
print('Задание №1 - Рекурсионный подсчёт отрицательных чисел в списке')

c = 0


def func(x):
    global c
    for i in x:
        if i < 0:
            c += 1
            func(x[1:])
            return c
        else:
            func(x[1:])
            return c


ds = [randint(-10, 10) for i in range(10)]
print(ds)
print(func(ds))

print(liner * 7)
print('Задание №2 - Работа и сортировка списков различными вариантами')


def shell_sort(s):
    gap = len(s)

    while gap > 0:
        for val in range(gap, len(s)):
            cur_val = s[val]
            pos = val

            while pos >= gap and s[pos - gap] > cur_val:
                s[pos] = s[pos - gap]
                pos -= gap
                s[pos] = cur_val

        gap //= 2

    return s


def shell_sort1(s):
    gap = len(s)

    while gap > 0:
        for val in range(gap, len(s)):
            cur_val = s[val]
            pos = val

            while pos >= gap and s[pos - gap] < cur_val:
                s[pos] = s[pos - gap]
                pos -= gap
                s[pos] = cur_val

        gap //= 2

    return s


def merge_sort(a):
    n = len(a)
    if n < 2:
        return a
    l = merge_sort(a[:n // 2])
    r = merge_sort(a[n // 2:n])
    i = j = 0
    res = []
    while i < len(l) or j < len(r):
        if not i < len(l):
            res.append(r[j])
            j += 1
        elif not j < len(r):
            res.append(l[i])
            i += 1
        elif l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    return res


def merge_sort12(a):
    n = len(a)
    if n < 2:
        return a

    l = merge_sort12(a[:n // 2])
    r = merge_sort12(a[n // 2:n])
    i = j = 0
    res = []
    while i < len(l) or j < len(r):
        if not i < len(l):
            res.append(r[j])
            j += 1
        elif not j < len(r):
            res.append(l[i])
            i += 1
        elif l[i] > r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    return res


def bubble(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def bubble1(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def sup_func(*args):
    cts = []
    for i in args:
        cts += i
    print(cts)
    ch = int(input('Введите способ сортировки и порядок:\n'
                   '1- Пузырьковая сортировка по возрастанию\n'
                   '2- Пузырьковая сортировка по убыванию\n'
                   '3- Быстрая сортировка по возрастанию\n'
                   '4- Быстрая сортировка по убыванию\n'
                   '5- Сортировка Шелла по возрастанию\n'
                   '6- Сортировка Шелла по убыванию\n'
                   
                   '-->'))
    if ch == 1:
        bubble(cts)
        print(cts)
    if ch == 2:
        bubble1(cts)
        print(cts)
    if ch == 3:
        cts = merge_sort(cts)
        print(cts)
    if ch == 4:
        cts = merge_sort12(cts)
        print(cts)
    if ch == 5:
        shell_sort(cts)
        print(cts)
    if ch == 6:
        shell_sort1(cts)
        print(cts)


a = [randint(1, 99) for y in range(5)]
b = [randint(1, 99) for y in range(5)]
c = [randint(1, 99) for y in range(5)]
d = [randint(1, 99) for y in range(5)]
sup_func(a, b, c, d)


