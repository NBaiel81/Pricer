from django.db import models


class Firm(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название', unique=True)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    logotype = models.ImageField(blank=True, null=True, verbose_name='Картинки', default='pricer_default.jpg')


class Product(models.Model):
    categories = (
        ('metal', 'metal'),
        ('not_metal', 'not_metal'),
    )
    image = models.ImageField(blank=True, null=True, verbose_name='Картинки', default='pricer_default.jpg')
    name = models.CharField(max_length=40, verbose_name='Название', unique=True)
    category = models.CharField(max_length=40, choices=categories, verbose_name='Категория', blank=True)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Стоимость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
