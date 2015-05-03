# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20150502_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='public_phone',
            field=models.CharField(max_length=11, null=True, blank=True),
            preserve_default=True,
        ),
    ]
