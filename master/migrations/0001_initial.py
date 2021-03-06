# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('pub', models.DateTimeField(verbose_name=b'Date Published')),
                ('one', models.CharField(max_length=200)),
                ('two', models.CharField(max_length=200)),
                ('three', models.CharField(max_length=200)),
                ('five', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
