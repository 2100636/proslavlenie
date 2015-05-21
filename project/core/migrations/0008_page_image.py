# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150521_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(default='', upload_to=b'articles/images/', verbose_name='\u0411\u0430\u043d\u0435\u0440', blank=True),
            preserve_default=False,
        ),
    ]
