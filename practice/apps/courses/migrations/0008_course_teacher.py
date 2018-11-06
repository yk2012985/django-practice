# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-11-02 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_teacher_image'),
        ('courses', '0007_video_play_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='授课教师'),
        ),
    ]