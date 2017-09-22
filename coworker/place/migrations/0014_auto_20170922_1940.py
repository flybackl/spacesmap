# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0013_place_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='cs_extra_description',
        ),
        migrations.RemoveField(
            model_name='place',
            name='meeting_room_number',
        ),
        migrations.AlterField(
            model_name='place',
            name='space_name',
            field=models.CharField(max_length=250, verbose_name='创客云图场地的名称'),
        ),
        migrations.AlterField(
            model_name='place',
            name='user_type',
            field=models.CharField(choices=[('ot', '官方团队'), ('cm', '新会员'), ('pm', '老会员')], default='ot', max_length=2),
        ),
    ]
