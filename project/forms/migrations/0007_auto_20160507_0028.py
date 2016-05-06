# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20160507_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hvalascool',
            name='date_test',
            field=models.DateField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f_', editable=False),
            preserve_default=True,
        ),
    ]
