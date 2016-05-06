# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_auto_20160506_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='biblescool',
            name='test',
            field=models.CharField(default=b'---', max_length=200, verbose_name='test'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hvalascool',
            name='leader_fi',
            field=models.CharField(max_length=255, verbose_name='\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0424.\u0418. \u043b\u0438\u0434\u0435\u0440\u0430, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043c\u043e\u0436\u0435\u0442 \u043f\u043e\u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u0442\u044c \u0432\u0430\u0441 \u0434\u043b\u044f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f, \u0435\u0433\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d'),
            preserve_default=True,
        ),
    ]
