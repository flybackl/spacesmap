# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0015_meetingroom_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetingroom',
            options={'verbose_name': 'Meeting Room', 'verbose_name_plural': 'Meeting Rooms'},
        ),
        migrations.RemoveField(
            model_name='place',
            name='cityLat',
        ),
        migrations.RemoveField(
            model_name='place',
            name='cityLng',
        ),
        migrations.AddField(
            model_name='place',
            name='lat',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='place',
            name='lng',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='place',
            name='address_sec',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='place',
            name='area',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='place',
            name='postal_code',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
