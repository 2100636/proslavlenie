# -*- coding: utf-8 -*-
from django.db import models
import datetime

class BibleScool(models.Model):
    fio = models.CharField(max_length=100, verbose_name=u'Ф.И.О')
    birth_day = models.DateField(verbose_name=u'Дата рождения')
    phone = models.CharField(max_length=11, verbose_name=u'Контактный телефон')
    city = models.CharField(max_length=200, verbose_name=u'Город проживания')
    family_status = models.CharField(max_length=200, verbose_name=u'Семейное положение')
    test = models.CharField(max_length=200, verbose_name=u'test', default='---' )

    you_church = models.CharField(max_length=240, verbose_name=u'К какой Церкви Вы принадлежите')
    church_city = models.CharField(max_length=200, verbose_name=u'Город')
    pastor_fio = models.CharField(max_length=100, verbose_name=u'Ф.И.О пастора Церкви')
    is_church_member = models.BooleanField(default=False, verbose_name=u'Являетесь ли Вы членом Церкви')
    is_believer = models.BooleanField(default=False, verbose_name=u'Веруете ли Вы в Иисуса Христа как своего Господа и Спасителя')
    salvation_day = models.DateTimeField(verbose_name=u'Дата Вашего спасения')

    you_mission = models.TextField(verbose_name=u'Чувствуете ли Вы ясное призвание от Бога на служение? Если да, то какое?')

    form_of_study = models.CharField(
        max_length=200,
        verbose_name=u'Форма обучения',
        choices=(
            ('day', 'дневная'),
            ('evening', 'вечерняя')
        ),
        default='day')

    rules = models.BooleanField(verbose_name=u'Я понимаю, что, как слушатель Библейских курсов, я обязан следовать установленным правилам.')

    class Meta:
        verbose_name = u'Заполненная форма билейской школы'
        verbose_name_plural = u'Заполненные формы библейской школы'

    def __unicode__(self):
        return u'%s - форма БШ' % self.fio


class HvalaScool(models.Model):
    fi = models.CharField(max_length=100, verbose_name=u'Ф.И.')
    city = models.CharField(max_length=200, verbose_name=u'Город, название церкцви')
    phone = models.CharField(max_length=11, verbose_name=u'Телефон (по которому с вами можно связаться в любое время)')
    age = models.IntegerField(verbose_name=u'Возраст (полных лет)')
    music_education = models.CharField(max_length=255, verbose_name=u'Музыкальное образование, специальность, дата окончания')
    how_class = models.CharField(max_length=200,
        choices=(
            ('klav_vokal', 'Клавиши + вокал'),
            ('gitar_vokal', 'Гитара + вокал'),
            ('basgitara', 'Бас-гитара'),
            ('baraban', 'Барабаны')
        ),
        verbose_name=u'Укажите класс, в котором планируете обучаться'
    )
    type_ministry = models.CharField(max_length=255, verbose_name=u'Укажите, в каком служении применять полученные знания после окончания Школы Хвалы')
    leader_fi = models.CharField(max_length=255, verbose_name=u'Укажите Ф.И. лидера, который может порекомендовать вас для обучения, его телефон')
    date = models.DateField(verbose_name=u'Дата заполнения', default=datetime.datetime.now, editable=False)
    class Meta:
        verbose_name = u'Анкета для поступления в Школу Хвалы'
        verbose_name_plural = u'Анкеты для поступления в Школу Хвалы'

    def __unicode__(self):
        return u'%s - Анкета' % self.fi

