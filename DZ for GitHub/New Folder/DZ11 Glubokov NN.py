from random import randint

liner = '---------------'
print(liner * 7)
print('Задание №1 - обрезание кортежа по искомому нам числу')

sd = tuple([randint(0, 10) for i in range(12)])

print(sd)


def slicer(x, y):
    lst = []
    for v in x:
        for i in range(len(x)):
            if x[i] == y:
                lst.append(i)
        if len(lst) == 1:
            lst.append(len(x))
        if len(lst) == 0:
            print('Dannogo chisla net v kortege')
            x1 = ()
            return x1
    x1 = x[lst[0]:lst[1] + 1]
    return x1


print(slicer(sd, 4))
print(liner * 7)
print('Задание №2 - поиск нулей в собранном кортеже')


def cort(x=0):
    if x == 1:
        s = tuple([randint(0, 5) for i in range(10)])
    else:
        s = tuple([randint(-5, 0) for i in range(10)])
    return s


cr1 = cort(1)
cr2 = cort()
print('Первый кортеж: ',cr1)
print('Второй кортеж: ',cr2)

cr3 = cr1 + cr2
print('Новый кортеж: ', cr3)

print('Количество нулей в нашем новом кортеже:', cr3.count(0))
