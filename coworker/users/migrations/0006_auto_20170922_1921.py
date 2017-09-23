# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170922_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='industry',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Industry'),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration',
            field=models.DateField(blank=True, null=True, verbose_name='Registration'),
        ),
    ]
