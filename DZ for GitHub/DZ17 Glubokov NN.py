from math import *
from random import *

liner = '---------------'

print(liner * 7)
print('Задание №1 - произведение значения списка на кубическое значение порядкового номера в списке')
s = [randint(1, 10) for i in range(10)]
print(s)
print(list(map(lambda x, y: x * y ** 3, s, range(len(s) + 1))))

print(liner * 7)
print('Задание №2 - Сумма всех отрицательных чисел по модулю')
s = [randint(-10, 10) for i in range(10)]
print(s)
print('Сумма всех отрицательных чисел по модулю равна', abs(sum(filter(lambda x: x < 0, s))))

print(liner * 7)
print('Задание №3 - возведение в квадрат и куб значений списка')
s = [randint(1, 10) for i in range(10)]
print(s)
print(list(map(lambda x: x ** 2, s)))
print(list(map(lambda x: x ** 3, s)))

print(liner * 7)
print('Задание №4 - двойная функция')


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
