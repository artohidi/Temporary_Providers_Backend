# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import tracking.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0005_auto_20170519_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='picture_1',
        ),
        migrations.AddField(
            model_name='provider',
            name='picture_12',
            field=models.ImageField(blank=True, null=True, upload_to=tracking.models.directory_path, verbose_name='تصویر پشت کارت ملی'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='picture_11',
            field=models.ImageField(blank=True, null=True, upload_to=tracking.models.directory_path, verbose_name='تصویر روی کارت ملی'),
        ),
    ]
