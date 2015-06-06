#-*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField


class IndexBlock(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=u'Название блока',
        help_text=u'Необходямо для отображения корректного названия\
            в админке',
        blank=False)

    content = RichTextField(
        help_text=u'При добавлении фотографии убедиться что фотография\
            находится только внутри тега <span style="color:red;">p</span><br/>\
            <span style="color:black;">ВАЖНО:</span> при добавлении фотографии\
            убедитесь что поля ширины и высоты - пустые',)
    description = models.CharField(
        max_length=200,
        verbose_name=u'Описание блока (синяя область)',
        blank=True)

    link = models.CharField(
        max_length=240,
        verbose_name=u'Ссылка на материал (не обязательно)',
        help_text=u'Обязательно писать абсолютную ссылку,\
            например : <span style="color:black;">http://hram.proslavlenie.ru/index.php/ru/</span>',
        blank=True)

    class Meta:
        verbose_name = u'Блок на главной'
        verbose_name_plural = u'Блоки на главной странице'

    def __unicode__(self):
        return u"%s - блок на главной" % self.name
