# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexblock',
            name='description',
            field=models.CharField(default='', max_length=200, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0431\u043b\u043e\u043a\u0430 (\u0441\u0438\u043d\u044f\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c)', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexblock',
            name='link',
            field=models.CharField(default='', max_length=50, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b (\u043d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indexblock',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u043b\u043e\u043e\u043a\u0430 \u0434\u043b\u044f \u0430\u0434\u043c\u0438\u043d\u043a\u0438'),
            preserve_default=True,
        ),
    ]
