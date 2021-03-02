# Generated by Django 3.1.6 on 2021-02-18 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_auto_20210218_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='firm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.firm', verbose_name='Фирма'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.productmodel', verbose_name='Модель'),
        ),
    ]
