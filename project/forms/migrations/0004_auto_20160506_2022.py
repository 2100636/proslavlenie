# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_hvalascool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hvalascool',
            name='how_class',
            field=models.CharField(max_length=200, verbose_name='\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043a\u043b\u0430\u0441\u0441, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u043f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u0442\u0435 \u043e\u0431\u0443\u0447\u0430\u0442\u044c\u0441\u044f', choices=[(b'klav_vokal', b'\xd0\x9a\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x88\xd0\xb8 + \xd0\xb2\xd0\xbe\xd0\xba\xd0\xb0\xd0\xbb'), (b'gitar_vokal', b'\xd0\x93\xd0\xb8\xd1\x82\xd0\xb0\xd1\x80\xd0\xb0 + \xd0\xb2\xd0\xbe\xd0\xba\xd0\xb0\xd0\xbb'), (b'basgitara', b'\xd0\x91\xd0\xb0\xd1\x81-\xd0\xb3\xd0\xb8\xd1\x82\xd0\xb0\xd1\x80\xd0\xb0'), (b'baraban', b'\xd0\x91\xd0\xb0\xd1\x80\xd0\xb0\xd0\xb1\xd0\xb0\xd0\xbd\xd1\x8b')]),
            preserve_default=True,
        ),
    ]
