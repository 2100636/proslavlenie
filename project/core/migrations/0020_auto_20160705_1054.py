# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_slideritem_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slideritem',
            options={'ordering': ['sort'], 'verbose_name': '\u0421\u043b\u0430\u0439\u0434', 'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439'},
        ),
    ]
