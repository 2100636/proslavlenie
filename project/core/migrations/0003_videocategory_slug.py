# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_ministry_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocategory',
            name='slug',
            field=models.CharField(default='', max_length=20, verbose_name='\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=False,
        ),
    ]
