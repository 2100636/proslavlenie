# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20150620_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='meta_description',
            field=models.CharField(max_length=200, verbose_name='\u041c\u0435\u0442\u0430 description \u0434\u043b\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='meta_title',
            field=models.CharField(max_length=80, verbose_name='\u041c\u0435\u0442\u0430 title \u0434\u043b\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
            preserve_default=True,
        ),
    ]
