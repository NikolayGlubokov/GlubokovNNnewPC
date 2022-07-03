from math import *
from random import *
import re

liner = '---------------'
print(liner * 7)
print('Задание №1 - Валидация номера телефона')
s = '+7 499 456 45 78 +74994564578 7 (499) 456 45 78 7 (499) 456-45-78'
reg = r'\+?[0-9]+\s?[(]?[0-9]{3}[)]?\s?[0-9]{3}[\s-]?[0-9]{2}[\s-]?[0-9]{2}'
print(re.findall(reg, s))

print(liner * 7)
print('Задание №2 - Задача на обход рекурсии. Подсчет количества имён в сложном списке')
names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']


def count_items(lst):
    lst = str(lst)
    reg1 = r'[a-zA-Z]+'
    print(re.findall(reg1, lst))
    return re.findall(reg1, lst)


print('Количество имён в сложном списке: ', len(count_items(names)))
