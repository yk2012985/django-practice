# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-01 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_lesson_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='play_times',
            field=models.IntegerField(default=0, verbose_name='时长（分钟数）'),
        ),
    ]