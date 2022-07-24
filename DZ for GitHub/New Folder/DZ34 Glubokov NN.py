from specgeometry import circle, cylinder, rectangle
from random import randint


def homework34():
    n = int(input('Введите количество кругов: '))
    m = int(input('Введите количество прямоугольников: '))
    k = int(input('Введите количество цилиндров: '))

    circle_lst = []
    cylinder_lst = []
    rectangle_lst = []

    for i in range(n):
        i = circle.Circle(randint(0,20))
        circle_lst.append(i)

    for i in circle_lst:
        print(f'Длина окружности: {i.perimeter_circle()}')

    for i in circle_lst:
        print(f'Площадь круга равна: {i.area()}')

    for i in range(k):
        i = rectangle.Rectangle(randint(0,20), randint(0,20))
        rectangle_lst.append(i)

    for i in rectangle_lst:
        print(f'Периметр прямоугольника: {i.perimeter()}')

    for i in range(m):
        i = cylinder.Cylinder(randint(0,20),randint(0,20), randint(0,20))
        cylinder_lst.append(i)
    print(cylinder_lst)
    for i in cylinder_lst:
        print(f'Площадь круга равна: {i.area_circle()}')
        print(f'Объём цилиндра равен: {i.value()}')


    print('Окружность с наибольшей площадью:', f'Радиус: {max([circle_lst[i].r for i in range(len(circle_lst))])}')
    print(f'Прямоугольник с наименьшим периметром:', min([rectangle_lst[i].perimeter() for i in range(len(rectangle_lst))]))
    print(f'Средний объём всех цилиндров:', round(sum([cylinder_lst[i].value() for i in range(len(cylinder_lst))])/len(cylinder_lst),2))


homework34()
