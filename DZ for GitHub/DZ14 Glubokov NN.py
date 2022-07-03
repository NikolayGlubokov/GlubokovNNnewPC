from random import randint

liner = '---------------'
print(liner * 7)
print('Задание №1 - создание словаря из двух одинаковых списков')
a = ['red', 'green', 'blue']
b = ['#FF0000', '#008000', '#0000FF']
c = dict(zip(a, b))
print(c)
print(liner * 7)
print('Задание №2 - создание словаря с кубами')
a = [i for i in range(1, 11)]
b = [i ** 3 for i in range(1, 11)]
c = dict(zip(a, b))
print(c)
print(liner * 7)
print('Задание №3 - создание словаря из двух одинаковых списков при помощи генератора словаря')
a = ['color', 'fruit', 'pet']
b = ['blue', 'apple', 'dog']
c = {key: value for (key, value) in zip(a, b)}
print(c)

print(liner * 7)
print('Задание №4 и №5 - нахождение минимального значения произвольного количества аргументов, а так же прогрессирующей суммы')

d = [[randint(1, 10) for j in range(int(input('Vvedite kolichestvo elementov v spiske: ')))] for i in range(int(input(
    'Vvedite kolichestvo elementov v osnovnom spiske: ')))]  # Я использовал списки, потому что данный сложный список использую и в 5-й задаче
for i in d:
    print(i)
# Хотя, я так и не понял - какой тип данных нужно использовать вообще в последних двух задачах. Потому что они не похожи на то, что
# я должен использовать set, tuple, или dict.
g = []
for i in range(len(d)):
    print('Минимальный аргумент в ' + str(i+1) + '-й строке равен:', min(d[i]))

for i in d:
    p = []
    for j in range(len(i)):
        s = sum(i[0:j + 1])
        p.append(s)
    g.extend([p])

    
for i in g:
    print(i)
