# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_auto_20170311_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='elo',
            field=models.FloatField(default=1200),
        ),
    ]
