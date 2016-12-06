# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-06 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teofibotweb', '0006_auto_20161205_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='NOT LABELED', max_length=200)),
                ('file_id', models.CharField(max_length=200, unique=True)),
                ('is_cool', models.BooleanField(default=False)),
            ],
        ),
    ]
