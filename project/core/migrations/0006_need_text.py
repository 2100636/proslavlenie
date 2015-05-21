# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150518_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='need',
            name='text',
            field=models.TextField(default='', verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f'),
            preserve_default=False,
        ),
    ]
