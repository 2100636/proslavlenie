# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20150502_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='photo',
            field=models.ImageField(default='', upload_to=b'authentication'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='public_phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
