# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-30 20:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200310_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='display_name',
            new_name='artist_name',
        ),
    ]