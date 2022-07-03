import os.path
import os
from math import *
from random import *
import re
import time


class Books:
    title = ''
    release = ''
    publisher = ''
    genre = ''
    author = ''
    price = ''

    def books_info(self):
        print("*"*40)
        print(
            f'Название книги: {self.title}\nГод выпуска: {self.release}\nИздательство: {self.publisher}\nЖанр:'
            f' {self.genre}\nАвтор: {self.author}\nЦена книги: {self.price}')
        print("*" * 40)

    def info_books(self, t, r, p, g, a, pr):
        self.title = t
        self.release = r
        self.publisher = p
        self.genre = g
        self.author = a
        self.price = pr

    def set_title(self, t):
        self.title = t

    def set_release(self, r):
        self.release = r

    def set_publisher(self, p):
        self.publisher = p

    def set_genre(self, g):
        self.genre = g

    def set_author(self, a):
        self.author = a

    def set_price(self, pr):
        self.price = pr

    def get_title(self):
        print(self.title)

    def get_release(self):
        print(self.release )

    def get_publisher(self):
        print(self.publisher)

    def get_genre(self):
        print(self.genre)

    def get_author(self):
        print(self.author)

    def get_price(self):
        print(self.price)


b1 = Books()

b1.info_books('Финансист', "2019", "Азбука-Аттикус", "Роман", "Теодор Дрейзен", "219")
b1.books_info()
b1.get_title()
b1.get_release()
b1.get_publisher()
b1.get_genre()
b1.get_author()
b1.get_price()

b1.set_title("Божественная комедия")
b1.set_release("2016")
b1.set_publisher("Издательство АСТ")
b1.set_genre("Поэма")
b1.set_author("Данте Алигьери")
b1.set_price("390")

b1.books_info()

b1.get_title()
b1.get_release()
b1.get_publisher()
b1.get_genre()
b1.get_author()
b1.get_price()

