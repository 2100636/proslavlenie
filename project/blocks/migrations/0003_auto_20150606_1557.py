# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0002_auto_20150606_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indexblock',
            options={'verbose_name': '\u0411\u043b\u043e\u043a \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439', 'verbose_name_plural': '\u0411\u043b\u043e\u043a\u0438 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435'},
        ),
        migrations.AlterField(
            model_name='indexblock',
            name='content',
            field=ckeditor.fields.RichTextField(help_text='\u041f\u0440\u0438 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0438 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0443\u0431\u0435\u0434\u0438\u0442\u044c\u0441\u044f \u0447\u0442\u043e \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f            \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u043d\u0443\u0442\u0440\u0438 \u0442\u0435\u0433\u0430 <span style="color:red;">p</span><br/>            <span style="color:black;">\u0412\u0410\u0416\u041d\u041e:</span> \u043f\u0440\u0438 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0438 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438            \u0443\u0431\u0435\u0434\u0438\u0442\u0435\u0441\u044c \u0447\u0442\u043e \u043f\u043e\u043b\u044f \u0448\u0438\u0440\u0438\u043d\u044b \u0438 \u0432\u044b\u0441\u043e\u0442\u044b - \u043f\u0443\u0441\u0442\u044b\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='indexblock',
            name='link',
            field=models.CharField(help_text='\u041e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u043f\u0438\u0441\u0430\u0442\u044c \u0430\u0431\u0441\u043e\u043b\u044e\u0442\u043d\u0443\u044e \u0441\u0441\u044b\u043b\u043a\u0443,            \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 : <span style="color:black;">http://hram.proslavlenie.ru/index.php/ru/</span>', max_length=240, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b (\u043d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='indexblock',
            name='name',
            field=models.CharField(help_text='\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u044f\u043c\u043e \u0434\u043b\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e\u0433\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f            \u0432 \u0430\u0434\u043c\u0438\u043d\u043a\u0435', max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u043b\u043e\u043a\u0430'),
            preserve_default=True,
        ),
    ]
