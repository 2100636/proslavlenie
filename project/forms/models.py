# -*- coding: utf-8 -*-
from django.db import models
import datetime

class BibleScool(models.Model):
    fio = models.CharField(max_length=100, verbose_name=u'Ф.И.О')
    birth_day = models.DateField(verbose_name=u'Дата рождения')
    phone = models.CharField(max_length=11, verbose_name=u'Контактный телефон')
    city = models.CharField(max_length=200, verbose_name=u'Город проживания')
    family_status = models.CharField(max_length=200, verbose_name=u'Семейное положение')

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

    rules = models.BooleanField(verbose_name=u'Я понимаю, что, как слушатель Библейских курсов, я обязан следовать установленным правилам.', default=True)
    agreement = models.BooleanField(verbose_name=u'Я ознакомлен(а) и согласен(а) с пользовательским соглашением об использовании персональных данных', default=True)

    class Meta:
        verbose_name = u'Заполненная форма библейской школы (курсы)'
        verbose_name_plural = u'Заполненные формы библейской школы (курсы)'

    def __unicode__(self):
        return u'%s - форма БШ' % self.fio


class HvalaScool(models.Model):
    fi = models.CharField(max_length=100, verbose_name=u'Ф.И.')
    city = models.CharField(max_length=200, verbose_name=u'Город, название церкви')
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
    date_test = models.DateField(verbose_name=u'Дата заполнения_', default=datetime.datetime.now, editable=False)
    agreement = models.BooleanField(verbose_name=u'Я ознакомлен(а) и согласен(а) с пользовательским соглашением об использовании персональных данных', default=True)
    
    class Meta:
        verbose_name = u'Анкета для поступления в Школу Хвалы'
        verbose_name_plural = u'Анкеты для поступления в Школу Хвалы'

    def __unicode__(self):
        return u'%s - Анкета' % self.fi




class PenuelConf(models.Model):
    fio = models.CharField(max_length=100, verbose_name=u'Ф.И.О')
    city = models.CharField(max_length=200, verbose_name=u'Город')
    phone = models.CharField(max_length=11, verbose_name=u'Телефон')
    email = models.CharField(max_length=30, verbose_name=u'E-mail')
    you_church = models.CharField(max_length=250, verbose_name=u'Название церкви')
    you_sluzhenie = models.CharField(max_length=250, verbose_name=u'Ваше служение')
    date = models.DateField(verbose_name=u'Дата заполнения', default=datetime.datetime.now, editable=False)

    class Meta:
        verbose_name = u'Анкета для конференции Пенуэл в Томске'
        verbose_name_plural = u'Анкеты для конференции Пенуэл в Томске'

    def __unicode__(self):
        return u'%s - Анкета' % self.fio









class Play2017(models.Model):
    fio = models.CharField(max_length=100, verbose_name=u'ФИО')
    age = models.IntegerField(verbose_name=u'Возраст (полных лет)') 
    sex = models.CharField(max_length=200,
        choices=(
            ('male', 'Мужской'),
            ('female', 'Женский')
        ),
        verbose_name=u'Пол'
    )    
    city = models.CharField(max_length=200, verbose_name=u'Город')
    you_church = models.CharField(max_length=240, verbose_name=u'Название церкви')
    pastor_fio = models.CharField(max_length=100, verbose_name=u'ФИО старшего пастора')
    whoiam = models.CharField(max_length=200,
        choices=(
            ('male', 'Молодежный пастор'),
            ('female', 'Подростковый пастор')
            ('male', 'Молодежный лидер'),
            ('male', 'Подростковый лидер'),
            ('male', 'Служение прославлени'),
            ('male', 'Администрирование'),
            ('male', 'Медиа'),
            ('male', 'Другое (указать)'),      
        ),
        verbose_name=u'Кем вы являетесь на данный момент '
    )   
    whoiam_custom = models.CharField(max_length=100, verbose_name=u'Кем вы являетесь на данный момент (Указать)', default='')
    agreement = models.BooleanField(verbose_name=u'Я ознакомлен(а) и согласен(а) с пользовательским соглашением об использовании персональных данных', default=True)

    class Meta:
        verbose_name = u'Заполненная форма PLAY 2017'
        verbose_name_plural = u'Заполненные формы PLAY 2017'

    def __unicode__(self):
        return u'%s - Анкета' % self.fio


