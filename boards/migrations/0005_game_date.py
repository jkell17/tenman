# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 04:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20170311_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 3, 11, 4, 30, 9, 412598)),
        ),
    ]
