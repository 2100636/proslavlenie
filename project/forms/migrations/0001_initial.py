# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BibleScool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fio', models.CharField(max_length=100, verbose_name='\u0424.\u0418.\u041e')),
                ('birth_day', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('phone', models.CharField(max_length=11, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('city', models.CharField(max_length=200, verbose_name='\u0413\u043e\u0440\u043e\u0434 \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u0438\u044f')),
                ('family_status', models.CharField(max_length=200, verbose_name='\u0421\u0435\u043c\u0435\u0439\u043d\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435')),
                ('you_church', models.CharField(max_length=240, verbose_name='\u041a \u043a\u0430\u043a\u043e\u0439 \u0426\u0435\u0440\u043a\u0432\u0438 \u0412\u044b \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u0438\u0442\u0435')),
                ('church_city', models.CharField(max_length=200, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('pastor_fio', models.CharField(max_length=100, verbose_name='\u0424.\u0418.\u041e \u043f\u0430\u0441\u0442\u043e\u0440\u0430 \u0426\u0435\u0440\u043a\u0432\u0438')),
                ('is_church_member', models.BooleanField(default=False, verbose_name='\u042f\u0432\u043b\u044f\u0435\u0442\u0435\u0441\u044c \u043b\u0438 \u0412\u044b \u0447\u043b\u0435\u043d\u043e\u043c \u0426\u0435\u0440\u043a\u0432\u0438')),
                ('is_believer', models.BooleanField(default=False, verbose_name='\u0412\u0435\u0440\u0443\u0435\u0442\u0435 \u043b\u0438 \u0412\u044b \u0432 \u0418\u0438\u0441\u0443\u0441\u0430 \u0425\u0440\u0438\u0441\u0442\u0430 \u043a\u0430\u043a \u0441\u0432\u043e\u0435\u0433\u043e \u0413\u043e\u0441\u043f\u043e\u0434\u0430 \u0438 \u0421\u043f\u0430\u0441\u0438\u0442\u0435\u043b\u044f')),
                ('salvation_day', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0412\u0430\u0448\u0435\u0433\u043e \u0441\u043f\u0430\u0441\u0435\u043d\u0438\u044f')),
                ('you_mission', models.TextField(verbose_name='\u0427\u0443\u0432\u0441\u0442\u0432\u0443\u0435\u0442\u0435 \u043b\u0438 \u0412\u044b \u044f\u0441\u043d\u043e\u0435 \u043f\u0440\u0438\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0442 \u0411\u043e\u0433\u0430 \u043d\u0430 \u0441\u043b\u0443\u0436\u0435\u043d\u0438\u0435? \u0415\u0441\u043b\u0438 \u0434\u0430, \u0442\u043e \u043a\u0430\u043a\u043e\u0435?')),
                ('form_of_study', models.CharField(default=b'day', max_length=200, verbose_name='\u0424\u043e\u0440\u043c\u0430 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f', choices=[(b'day', b'\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xb2\xd0\xbd\xd0\xb0\xd1\x8f'), (b'evening', b'\xd0\xb2\xd0\xb5\xd1\x87\xd0\xb5\xd1\x80\xd0\xbd\xd1\x8f\xd1\x8f')])),
                ('rules', models.BooleanField(default=False, verbose_name='\u042f \u043f\u043e\u043d\u0438\u043c\u0430\u044e, \u0447\u0442\u043e, \u043a\u0430\u043a \u0441\u043b\u0443\u0448\u0430\u0442\u0435\u043b\u044c \u0411\u0438\u0431\u043b\u0435\u0439\u0441\u043a\u0438\u0445 \u043a\u0443\u0440\u0441\u043e\u0432, \u044f \u043e\u0431\u044f\u0437\u0430\u043d \u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u044c \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044b\u043c \u043f\u0440\u0430\u0432\u0438\u043b\u0430\u043c.')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0430 \u0431\u0438\u043b\u0435\u0439\u0441\u043a\u043e\u0439 \u0448\u043a\u043e\u043b\u044b',
                'verbose_name_plural': '\u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0435 \u0444\u043e\u0440\u043c\u044b \u0431\u0438\u0431\u043b\u0435\u0439\u0441\u043a\u043e\u0439 \u0448\u043a\u043e\u043b\u044b',
            },
            bases=(models.Model,),
        ),
    ]
