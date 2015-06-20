# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150620_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='article',
            name='meta_title',
        ),
    ]
