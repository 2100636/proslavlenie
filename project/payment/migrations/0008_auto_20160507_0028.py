# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20160506_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='customer_number',
            field=models.CharField(default=b'c9de1c047c8b439eb98910d817a1d629', max_length=64, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043b\u0430\u0442\u0435\u043b\u044c\u0449\u0438\u043a\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='payment',
            name='order_number',
            field=models.CharField(default=b'6abb9a663456470e975aa379558c7fde', max_length=64, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u043a\u0430\u0437\u0430'),
            preserve_default=True,
        ),
    ]
