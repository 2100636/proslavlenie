# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_auto_20160507_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hvalascool',
            name='city',
            field=models.CharField(max_length=200, verbose_name='\u0413\u043e\u0440\u043e\u0434, \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0446\u0435\u0440\u043a\u0432\u0438'),
            preserve_default=True,
        ),
    ]
