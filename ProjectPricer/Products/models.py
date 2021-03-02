from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True, blank=True, null=True)
    quantity = models.CharField(max_length=100,blank=True, null=True, verbose_name='Количество')
    price = models.CharField(max_length=100,blank=True, null=True, verbose_name='Цена')
    def __str__(self):
        return self.name
class Firm(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название', unique=True)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    logotype = models.ImageField(blank=True, null=True, verbose_name='Логотип', default='pegatec.jpg')
    def __str__(self):
        return self.name
class Product(models.Model):
    image = models.ImageField(blank=True, null=True, verbose_name='Картинки', default='pricer_default.jpg')
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.CharField(max_length=100, verbose_name='Стоимость', blank=True,null=True)
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True, verbose_name='Фирма', blank=True)
    product_model = models.ManyToManyField(ProductModel, blank=True, verbose_name='Модель')
    quantity = models.CharField(max_length=100,blank=True, null=True, verbose_name='Количество')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

class Footer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True, blank=True, null=True )
    text = models.TextField(blank=True, null=True, verbose_name='Описание')
    logotype = models.ImageField(blank=True, null=True, verbose_name='Картинки', default='pricer_default.jpg')
    def __str__(self):
        return self.name







