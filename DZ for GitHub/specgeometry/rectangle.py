class Rectangle:
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    def info(self):
        print(f'Ширина прямоугольника: {self.a}\n'
              f'Длина прямоугольника: {self.b}')

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)
