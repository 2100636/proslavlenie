# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='need',
            options={'verbose_name': '\u041d\u0443\u0436\u0434\u0430', 'verbose_name_plural': '\u041d\u0443\u0436\u0434\u044b'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430', 'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441', 'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b'},
        ),
        migrations.AlterModelOptions(
            name='videocategory',
            options={'verbose_name': '\u0412\u0438\u0434\u0435\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterField(
            model_name='pagegalleryimage',
            name='image',
            field=models.ImageField(upload_to=b'gallery_page', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0433\u0430\u043b\u0435\u0440\u0435\u0438', blank=True),
            preserve_default=True,
        ),
    ]
