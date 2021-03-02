# Generated by Django 3.1.6 on 2021-02-18 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_product_model_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Название')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='model_product',
        ),
        migrations.AlterField(
            model_name='footer',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='firm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.firm', verbose_name='firm'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.productmodel', verbose_name='model'),
        ),
    ]
