# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-05 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teofibotweb', '0005_textinputpattern_specialresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tag',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
