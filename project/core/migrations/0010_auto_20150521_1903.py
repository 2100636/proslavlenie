# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150521_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(b'image', '340x340', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagegalleryimage',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(b'image', '340x340', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping'),
            preserve_default=True,
        ),
    ]
