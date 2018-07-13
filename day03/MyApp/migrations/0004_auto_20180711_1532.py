# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-11 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_auto_20180711_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='h_birthday',
            field=models.DateTimeField(verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='h_gender',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别'),
        ),
    ]
