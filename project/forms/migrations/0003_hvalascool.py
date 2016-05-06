# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20150815_0343'),
    ]

    operations = [
        migrations.CreateModel(
            name='HvalaScool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fi', models.CharField(max_length=100, verbose_name='\u0424.\u0418.')),
                ('city', models.CharField(max_length=200, verbose_name='\u0413\u043e\u0440\u043e\u0434, \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0446\u0435\u0440\u043a\u0446\u0432\u0438')),
                ('phone', models.CharField(max_length=11, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d (\u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u0441 \u0432\u0430\u043c\u0438 \u043c\u043e\u0436\u043d\u043e \u0441\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0432 \u043b\u044e\u0431\u043e\u0435 \u0432\u0440\u0435\u043c\u044f)')),
                ('age', models.IntegerField(verbose_name='\u0412\u043e\u0437\u0440\u0430\u0441\u0442 (\u043f\u043e\u043b\u043d\u044b\u0445 \u043b\u0435\u0442)')),
                ('music_education', models.CharField(max_length=255, verbose_name='\u041c\u0443\u0437\u044b\u043a\u0430\u043b\u044c\u043d\u043e\u0435 \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435, \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c, \u0434\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f')),
                ('how_class', models.IntegerField(verbose_name='\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043a\u043b\u0430\u0441\u0441, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u043f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u0442\u0435 \u043e\u0431\u0443\u0447\u0430\u0442\u044c\u0441\u044f', choices=[(b'klav_vokal', b'\xd0\x9a\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x88\xd0\xb8 + \xd0\xb2\xd0\xbe\xd0\xba\xd0\xb0\xd0\xbb'), (b'gitar_vokal', b'\xd0\x93\xd0\xb8\xd1\x82\xd0\xb0\xd1\x80\xd0\xb0 + \xd0\xb2\xd0\xbe\xd0\xba\xd0\xb0\xd0\xbb'), (b'basgitara', b'\xd0\x91\xd0\xb0\xd1\x81-\xd0\xb3\xd0\xb8\xd1\x82\xd0\xb0\xd1\x80\xd0\xb0'), (b'baraban', b'\xd0\x91\xd0\xb0\xd1\x80\xd0\xb0\xd0\xb1\xd0\xb0\xd0\xbd\xd1\x8b')])),
                ('type_ministry', models.CharField(max_length=255, verbose_name='\u0423\u043a\u0430\u0436\u0438\u0442\u0435, \u0432 \u043a\u0430\u043a\u043e\u043c \u0441\u043b\u0443\u0436\u0435\u043d\u0438\u0438 \u043f\u0440\u0438\u043c\u0435\u043d\u044f\u0442\u044c \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0435 \u0437\u043d\u0430\u043d\u0438\u044f \u043f\u043e\u0441\u043b\u0435 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0428\u043a\u043e\u043b\u044b \u0425\u0432\u0430\u043b\u044b')),
                ('leader_fi', models.CharField(max_length=255, verbose_name='\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0424\u0418 \u043b\u0438\u0434\u0435\u0440\u0430, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043c\u043e\u0436\u0435\u0442 \u043f\u043e\u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u043e\u0432\u0430\u0442\u044c \u0432\u0430\u0441 \u0434\u043b\u044f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f, \u0435\u0433\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f', editable=False)),
            ],
            options={
                'verbose_name': '\u0410\u043d\u043a\u0435\u0442\u0430 \u0434\u043b\u044f \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0432 \u0428\u043a\u043e\u043b\u0443 \u0425\u0432\u0430\u043b\u044b',
                'verbose_name_plural': '\u0410\u043d\u043a\u0435\u0442\u044b \u0434\u043b\u044f \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0432 \u0428\u043a\u043e\u043b\u0443 \u0425\u0432\u0430\u043b\u044b',
            },
            bases=(models.Model,),
        ),
    ]
