# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 18:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_auto_20170519_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='picture',
            new_name='picture_0',
        ),
    ]