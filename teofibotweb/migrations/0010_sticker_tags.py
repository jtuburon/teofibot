# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-06 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teofibotweb', '0009_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticker',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='teofibotweb.Tag'),
        ),
    ]