# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150604_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='meta_description',
            field=models.TextField(default='', verbose_name='\u041c\u0435\u0442\u0430 description \u0434\u043b\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='meta_title',
            field=models.CharField(default='', max_length=200, verbose_name='\u041c\u0435\u0442\u0430 title \u0434\u043b\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name=b'cropping_pritch',
            field=image_cropping.fields.ImageRatioField(b'cover', '165x200', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='\u041e\u0431\u043b\u043e\u0436\u043a\u0430 \u043f\u0440\u043e\u043f\u043e\u0432\u0435\u0434\u0438 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439'),
            preserve_default=True,
        ),
    ]
