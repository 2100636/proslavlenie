# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20150620_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideritem',
            name='sort',
            field=models.IntegerField(default=0, help_text='\u0421\u043b\u0430\u0439\u0434\u044b \u0441\u043e\u0440\u0442\u0438\u0440\u0443\u044e\u0442\u0441\u044f \u0432 \u043f\u043e\u0440\u044f\u0434\u043a\u0435 \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u044f', verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438'),
            preserve_default=True,
        ),
    ]
