# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 22:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disk', '0012_disk_disk_shown'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disk',
            old_name='disk_name',
            new_name='disk_device',
        ),
    ]
