# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 00:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disk', '0008_disk_disk_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disk',
            name='disk_percent',
        ),
    ]