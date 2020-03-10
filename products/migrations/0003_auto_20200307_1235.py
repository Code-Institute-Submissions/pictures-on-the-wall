# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-07 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format_name', models.CharField(default='', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(default='10 x 15 cm', max_length=16)),
                ('longer_side', models.DecimalField(decimal_places=2, default=15, max_digits=3)),
                ('shorter_side', models.DecimalField(decimal_places=2, default=10, max_digits=3)),
            ],
        ),
        migrations.AlterField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='formats',
            name='size',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Sizes'),
        ),
    ]
