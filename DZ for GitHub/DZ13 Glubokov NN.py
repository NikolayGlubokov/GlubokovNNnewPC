liner = '---------------'
print(liner * 7)
print('Задание №1 - разделение словаря на два словаря')

d1 = {'name': 'Kelly', 'age': '25', 'salary': '8000', 'city': 'New York'}  # Исходный словарь
d11 = d1.copy()
s = list(d1.keys())  # введено для навигации по ключам словаря
s1 = list(d1.keys())  # введено для навигации по ключам словаря во втором задании

d = {}  # Пустые словари для заполнения
f = {}
k = {}

for i in range(len(d1)):
    if i % 2 == 0:
        d[s[i]] = d1[s[i]]
        d1.pop(s[i])
    # else:
    #     f[s[i]] = dicter[s[i]]    # можно заменить в задании, если исходный словарь не трогать. Изначально я с ним и сделал

print('Обновленный изначальный словарь:', d1)
print('Новый словарь:', d)

print(liner * 7)
print('Задание №2 - замена названия ключа в исходном словаре')

l = input('Введите название ключа, который хотите переименовать: ')
p = input('Введите новое название ключа, который вы переименовываете: ')

for i in range(len(d11)):
    if s[i] == l:
        s1[i] = p
    k[s1[i]] = d11[s[i]]
#
d11 = k.copy()
del k
print('Модифицированный словарь: ', d11)
# print(f)
# print(k)
