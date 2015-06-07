# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerFaq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField(verbose_name='\u041e\u0442\u0432\u0435\u0442 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441 \u0432 FAQ')),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0432\u0435\u0442 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441 \u0432 FAQ',
                'verbose_name_plural': '\u041e\u0442\u0432\u0435\u0442\u044b \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u0432 FAQ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionFaq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u0422\u0435\u043c\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u0430')),
                ('question', models.TextField(verbose_name='\u0417\u0430\u0434\u0430\u0439\u0442\u0435 \u0432\u043e\u043f\u0440\u043e\u0441')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441 \u0432 FAQ',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b \u0432 FAQ',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answerfaq',
            name='question',
            field=models.ForeignKey(to='faq.QuestionFaq'),
            preserve_default=True,
        ),
    ]
