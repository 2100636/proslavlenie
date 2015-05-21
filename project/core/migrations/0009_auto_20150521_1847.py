# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_page_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='entry',
            field=models.TextField(default='', verbose_name='\u0412\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='sub_title',
            field=models.CharField(default='', max_length=60, verbose_name='\u041f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
            preserve_default=False,
        ),
    ]
