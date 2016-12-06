# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-06 16:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teofibotweb', '0007_sticker'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticker',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='publication date'),
        ),
    ]
