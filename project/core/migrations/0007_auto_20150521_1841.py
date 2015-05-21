# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_need_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slider',
        ),
        migrations.AlterField(
            model_name='ministry',
            name='video',
            field=models.CharField(help_text='\u0432\u0432\u043e\u0434\u0438\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u0442\u0441\u044f \u0432 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0435         \u043d\u0430\u0436\u0430\u0442\u0438\u044f \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u043f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f \u0432 youtube, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440         "https://youtu.be/t42-71RpRgI?t=1h41m40s" ', max_length=200, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e youtube'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='link',
            field=models.CharField(help_text='\u0421\u0441\u044b\u043b\u043a\u0430 \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u0438                             \u043d\u0430\u0447\u0438\u043d\u0430\u0442\u044c\u0441\u044f \u0441 \u043a\u043e\u0440\u043d\u044f \u0441\u0430\u0439\u0442\u0430 \u0441\u043e \u0437\u043d\u0430\u043a\u0430 "/" \n \u043f\u0440\u0438\u043c\u0435\u0440 \u0441\u0441\u044b\u043b\u043a\u0438 "/news/1" ', max_length=200, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.CharField(help_text='\u0432\u0432\u043e\u0434\u0438\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u0442\u0441\u044f \u0432 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0435         \u043d\u0430\u0436\u0430\u0442\u0438\u044f \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u043f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f \u0432 youtube, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440         "https://youtu.be/t42-71RpRgI?t=1h41m40s" ', max_length=200, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e youtube'),
            preserve_default=True,
        ),
    ]
