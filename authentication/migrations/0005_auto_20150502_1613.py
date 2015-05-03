# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20150502_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'authentication', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='public_phone',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
