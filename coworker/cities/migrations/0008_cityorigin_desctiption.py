# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0007_cityorigin_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityorigin',
            name='desctiption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
