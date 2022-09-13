from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название населенного пункта")
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название населенного пункта"
        verbose_name_plural = "Названия населенных пунктов"


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Язык программирования")
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Язык программирования"
        verbose_name_plural = "Языки программирования"


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name="Название вакансии")
    company = models.CharField(max_length=250, verbose_name="Компания")
    description = models.TextField(verbose_name="Описание вакансии")
    city = models.ForeignKey("City", on_delete=models.CASCADE, verbose_name="Город")
    language = models.ForeignKey("Language", on_delete=models.CASCADE, verbose_name="Язык программирования")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['-timestamp']
