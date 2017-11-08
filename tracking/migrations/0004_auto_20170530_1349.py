# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_auto_20170530_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkdocument',
            options={'verbose_name': 'مدارک فردی', 'verbose_name_plural': 'مدارک فردی'},
        ),
        migrations.AlterModelOptions(
            name='conversationdetail',
            options={'verbose_name': 'فرم مصاحبه (فرم شماره ۲)', 'verbose_name_plural': 'فرم مصاحبه (فرم شماره ۲)'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'سرویس های قابل ارائه', 'verbose_name_plural': 'سرویس های قابل ارائه'},
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'verbose_name': 'فرم ثبت نام (فرم شماره ۱)', 'verbose_name_plural': 'فرم ثبت نام (فرم شماره ۱)'},
        ),
        migrations.AlterField(
            model_name='provider',
            name='basic_information',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='provider_basic_information', to='tracking.ProviderBasicInfo', verbose_name='اطلاعات پایه همکار جدید'),
        ),
    ]
