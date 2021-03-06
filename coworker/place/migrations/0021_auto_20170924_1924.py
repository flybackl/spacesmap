# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0020_auto_20170924_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='currency',
        ),
        migrations.AlterField(
            model_name='place',
            name='accs',
            field=models.BooleanField(default=True, verbose_name='Do you accept credit cards?'),
        ),
        migrations.AlterField(
            model_name='place',
            name='apps',
            field=models.BooleanField(default=True, verbose_name='Can members pay with PayPal?'),
        ),
        migrations.AlterField(
            model_name='place',
            name='deposit',
            field=models.CharField(max_length=250, verbose_name='eg. none, 1 month, etc'),
        ),
        migrations.AlterField(
            model_name='place',
            name='opay',
            field=models.BooleanField(default=True, verbose_name='Can members pay online?'),
        ),
    ]
