from django.db import models
from django.urls import reverse


class Parts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название детали')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    price = models.IntegerField()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('autoparts:part', kwargs={'part_slug': self.slug})

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('autoparts:category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
