# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disk', '0003_remove_disk_disk_usedsize'),
    ]

    operations = [
        migrations.AddField(
            model_name='disk',
            name='disk_size_used',
            field=models.IntegerField(default=0),
        ),
    ]
