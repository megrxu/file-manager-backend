# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disk', '0002_auto_20170412_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disk',
            name='disk_usedsize',
        ),
    ]