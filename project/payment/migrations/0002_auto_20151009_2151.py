# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='customer_number',
            field=models.CharField(default=b'648f00b3-26af-488b-873c-99700fda6881', max_length=64, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043b\u0430\u0442\u0435\u043b\u044c\u0449\u0438\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='order_number',
            field=models.CharField(default=b'c00eb938-8a10-46ce-a5f6-effab5048b82', max_length=64, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u043a\u0430\u0437\u0430'),
        ),
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together=set([]),
        ),
    ]
