from math import *
from random import *

liner = '---------------'
print(liner * 7)
print('Задание №1 - Создание функции с декоратором')  # Честно- получилось не с первого раза и вообще, началось со скрипом. Поэтому прошу вас
# прокоментировать правильность выполнения задачи


def decor(func):
    def wrap(*args):
        str3 = ''
        for i in args:
            if i != args[len(args) - 1]:
                str3 += str(i) + ', '
            else:
                str3 += str(i)
        print('Сумма чисел', str3, '=', func(*args))
        print('Среднее арифмметическое чисел', str3, '=', func(*args) / len(args))

    return wrap


@decor
def func(*args):
    s = sum(args)
    return s


func(1, 6, 9, 4)
print(liner * 7)
print(    'Задание №2 - Замена символа на другой')  # В данном задании отсчет был ныл начат с 1, так как отчет ведется не по индексам, как в списке, а по реальному наличию.

str1 = 'Я изучаю Nython. Мне нравится Nython. Nython мой любимый язык'
print(str1)


def func(x, s1, s2):
    str2 = ''
    s = 1
    for i in x:
        if s1 == i and s % 2 == 0:
            str2 += s2
            s += 1
        elif s1 == i and s % 2 != 0:
            str2 += i
            s += 1
        else:
            str2 += i
    print(str2)


func(str1, 'N', 'P')
print(liner * 7)
print('Задание №3 - Удаление символа по номеру позиции')

sls = input('введите упорядоченные значения: ')
d = int(input('номер позиции для удаления: '))
# Так как у нас присутствует упорядоченный список значений, то мы можем использовать порядок исчисления как в списках. Но
# если добавить поменять местами закоментированную строку с раскоментированной, то можно получить такой же порядок, как и в предыдущей задаче

def func(x, y):
    s2 = ''
    for i in range(len(x)):
        if y==i:
        #if y == i+1:
            pass
        else:
            s2 += x[i]
    return s2


print(func(sls, d))

print(liner * 7)
print('Задание №4 - Удаление всех вхождений заданного символа в строке')

s = input('введите какие-нибудь символы: ')
d = input('введите символ, входящий в данную строку, для его удаления: ')


def func(x, y):
    s2 = ''
    for i in x:
        if y == i:
            pass
        else:
            s2 += i
    return s2


print(func(s, d))
