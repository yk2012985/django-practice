# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-22 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20181021_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='wor_position',
            new_name='work_position',
        ),
    ]
