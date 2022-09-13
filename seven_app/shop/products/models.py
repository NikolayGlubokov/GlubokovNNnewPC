from django.db import models
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Категория')
    description = models.TextField(blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название товара')
    image = models.ImageField(upload_to='products_images', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Полное описание')
    short_description = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_database = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    class Meta:
        verbose_name = 'Товар в корзину'
        verbose_name_plural = 'Корзина'
