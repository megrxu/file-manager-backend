# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disk',
            name='disk_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='disk',
            name='disk_usedsize',
            field=models.IntegerField(default=0),
        ),
    ]
