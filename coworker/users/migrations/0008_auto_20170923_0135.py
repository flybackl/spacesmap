# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170922_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indastry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='industry',
        ),
        migrations.AddField(
            model_name='user',
            name='industries',
            field=models.ManyToManyField(blank=True, related_name='user', to='users.Indastry'),
        ),
    ]
