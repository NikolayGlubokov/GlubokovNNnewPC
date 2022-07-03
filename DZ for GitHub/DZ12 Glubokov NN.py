liner = '---------------'
print(liner * 7)
print('Задание №1 - выделение уникальных букв в первой строке, которых нет во второй')
a = set(input('Введите что-нибудь в первую строку: '))
b = set('Programming language')
l = set('pROGRAMMING LANGUAGE')  # переменная внесена для корректировки. Так как кодировка распознаёт большую и малую буквы как разные.
c = a - b - l
print('Уникальные буквы первой строки', c)

print(liner * 7)
print('Задание №2 - подсчёт гласных букв')  # Самая странная задача. делать через множества невозможно.
d = "аеёийоуыэюя"  # И всё из-за того, что в переменной "е", если вводить данные и даже если перевести в множество сокращаются буквы
e = input(
    'Напечатайте какую-нибудь строку: ')  # я использовал это в качестве проверки - "Напишите все буквы в первой строке, которые отсутствуют во второй"


def func(x, y):
    lst = []
    for i in x:
        for j in y:
            if i == j:
                lst.append(j)
    print('Количество глассных букв в строке: ', len(lst), '. В основном это: ', set(lst))


func(d, e)

print(liner * 7)
print('Задание №3 - объединение букв в строках')
i = set('test')
j = set('string')
print('Все буквы, присутствующие хотя бы в одной строке:', i | j)

print(liner * 7)
print('Задание №4 - удаление общих букв из двух букв ')
i = set('Hello')
j = set('world')
print('Уникальные буквы из двух строк:', i ^ j)
