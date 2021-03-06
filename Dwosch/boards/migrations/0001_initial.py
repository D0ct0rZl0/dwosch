# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-24 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractPostModel',
            fields=[
                ('date', models.DateField(auto_now=True, verbose_name='Дата постинга')),
                ('text', models.TextField(verbose_name='Текстовый контент треда')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название борды')),
                ('url', models.CharField(max_length=10, verbose_name='Адрес борды на сервере')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('abstractpostmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='boards.AbstractPostModel')),
            ],
            bases=('boards.abstractpostmodel',),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('abstractpostmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='boards.AbstractPostModel')),
            ],
            bases=('boards.abstractpostmodel',),
        ),
        migrations.AddField(
            model_name='abstractpostmodel',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_board', to='boards.Board'),
        ),
    ]
