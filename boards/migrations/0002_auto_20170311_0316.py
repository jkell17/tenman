# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='game',
            name='loser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loser', to='boards.Players'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='boards.Players'),
        ),
    ]
