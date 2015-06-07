# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerfaq',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 7, 21, 6, 44, 686260), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionfaq',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 7, 21, 6, 48, 374065), auto_now_add=True),
            preserve_default=False,
        ),
    ]
