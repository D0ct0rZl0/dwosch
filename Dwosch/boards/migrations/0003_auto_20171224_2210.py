# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-24 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20171224_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='url',
            field=models.CharField(max_length=10, unique=True, verbose_name='Адрес борды на сервере'),
        ),
    ]
