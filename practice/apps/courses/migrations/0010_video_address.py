# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-05 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20181102_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='address',
            field=models.URLField(default='', verbose_name='访问地址'),
        ),
    ]