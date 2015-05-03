# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import colorful.fields
import ckeditor.fields
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430')),
                ('slug', models.SlugField(unique=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('description', ckeditor.fields.RichTextField()),
                ('sub_title', models.CharField(max_length=60, verbose_name='\u041f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('entry', models.TextField(verbose_name='\u0412\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435')),
                ('image', models.ImageField(upload_to=b'articles/images/', verbose_name='\u0411\u0430\u043d\u0435\u0440', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '340x340', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleGalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'gallery_article', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0433\u0430\u043b\u0435\u0440\u0435\u0438', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '340x340', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                ('article', models.ForeignKey(to='core.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043b\u0443\u0436\u0435\u043d\u0438\u044f')),
                ('slug', models.SlugField(unique=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u043b\u0443\u0436\u0435\u043d\u0438\u0435')),
                ('video', models.CharField(help_text='\u0432\u0432\u043e\u0434\u0438\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u0442\u0441\u044f \u0432 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0435 \u043d\u0430\u0436\u0430\u0442\u0438\u044f \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u043f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f \u0432 youtube, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 "https://youtu.be/t42-71RpRgI?t=1h41m40s" ', max_length=200, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e youtube')),
                ('description', ckeditor.fields.RichTextField()),
                ('color', colorful.fields.RGBColorField()),
                ('allocate_description', models.TextField(verbose_name='\u0412\u044b\u0434\u0435\u043b\u0435\u043d\u044b\u0439 \u0431\u043b\u043e\u043a')),
                ('baner', models.ImageField(upload_to=b'ministry/images/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0433\u043e \u0431\u0430\u043d\u0435\u0440\u0430', blank=True)),
                ('baner_text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xbf\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd1\x85 \xd0\xb1\xd0\xb0\xd0\xbd\xd0\xb5\xd1\x80\xd0\xb0')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0443\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0421\u043b\u0443\u0436\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MinistryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'gallery_ministry', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0433\u0430\u043b\u0435\u0440\u0435\u0438 \u0441\u043b\u0443\u0436\u0435\u043d\u0438\u044f', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '175x175', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                ('ministry', models.ForeignKey(to='core.Ministry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438')),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to=b'news/images/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '275x200', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsGalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'gallery_news', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0433\u0430\u043b\u0435\u0440\u0435\u0438', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '175x120', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                ('news', models.ForeignKey(to='core.News')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430')),
                ('slug', models.SlugField(unique=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageGalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'gallery_page', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0433\u0430\u043b\u0435\u0440\u0435\u0438', blank=True)),
                ('page', models.ForeignKey(to='core.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u0418\u043c\u044f')),
                ('description', models.TextField(verbose_name='\u041e\u0442\u0437\u044b\u0432')),
                ('input_video', models.CharField(max_length=240, verbose_name='\u043f\u043e\u043b\u0435 \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438 \u0432\u0438\u0434\u0435\u043e \u0438\u0437 youtube', blank=True)),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430')),
                ('image', models.ImageField(upload_to=b'reviews', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '275x200', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0437\u044b\u0432',
                'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430')),
                ('link', models.CharField(help_text='\u0421\u0441\u044b\u043b\u043a\u0430 \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u0438 \u043d\u0430\u0447\u0438\u043d\u0430\u0442\u044c\u0441\u044f \u0441 \u043a\u043e\u0440\u043d\u044f \u0441\u0430\u0439\u0442\u0430 \u0441\u043e \u0437\u043d\u0430\u043a\u0430 "/" \n \u043f\u0440\u0438\u043c\u0435\u0440 \u0441\u0441\u044b\u043b\u043a\u0438 "/news/1" ', max_length=200, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430')),
                ('image', models.ImageField(upload_to=b'slider', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '880x320', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u0444\u043e\u0442\u043e')),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u0412\u0430\u0448\u0435 \u0438\u043c\u044f')),
                ('description', models.TextField(verbose_name='\u0412\u0430\u0448\u0435 \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e')),
                ('image', models.ImageField(upload_to=b'gallery_testimony', verbose_name='\u0424\u043e\u0442\u043e \u0434\u043b\u044f \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u0421\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e',
                'verbose_name_plural': '\u0421\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestimonyGalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'gallery_testimony', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0433\u0430\u043b\u0435\u0440\u0435\u0438', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '175x120', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                ('testimony', models.ForeignKey(to='core.Testimony')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('cover', models.ImageField(upload_to=b'covers', verbose_name='\u041e\u0431\u043b\u043e\u0436\u043a\u0430', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'cover', '479x320', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='\u041e\u0431\u043b\u043e\u0436\u043a\u0430 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0433\u043e \u0432\u0438\u0434\u0435\u043e \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439')),
                (b'cropping_pritch', image_cropping.fields.ImageRatioField(b'cover', '173x150', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='\u041e\u0431\u043b\u043e\u0436\u043a\u0430 \u043f\u0440\u043e\u043f\u043e\u0432\u0435\u0434\u0438 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439')),
                (b'cropping_videoblog', image_cropping.fields.ImageRatioField(b'cover', '275x200', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='\u041e\u0431\u043b\u043e\u0436\u043a\u0430 \u0432\u0438\u0434\u0435\u043e\u0431\u043b\u043e\u0433 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439')),
                ('video', models.CharField(help_text='\u0432\u0432\u043e\u0434\u0438\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u0442\u0441\u044f \u0432 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0435 \u043d\u0430\u0436\u0430\u0442\u0438\u044f \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u043f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f \u0432 youtube, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 "https://youtu.be/t42-71RpRgI?t=1h41m40s" ', max_length=200, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e youtube')),
            ],
            options={
                'verbose_name': '\u0412\u0438\u0434\u0435\u043e \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b',
                'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e \u043a\u043e\u043d\u0442\u0435\u043d\u0442',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u0438\u0434\u0435\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ForeignKey(verbose_name='\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u0434\u043b\u044f \u0432\u0438\u0434\u0435\u043e', blank=True, to='core.VideoCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='slider',
            field=models.OneToOneField(to='core.SliderItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='slider',
            field=models.OneToOneField(null=True, blank=True, to='core.SliderItem'),
            preserve_default=True,
        ),
    ]
