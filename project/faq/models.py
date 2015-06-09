#-*- coding: utf-8 -*-
from django.db import models
from authentication.models import Account


class QuestionFaq(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'Тема вопроса')
    question = models.TextField(verbose_name=u'Задайте вопрос')
    date = models.DateField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'Вопрос в FAQ'
        verbose_name_plural = u'Вопросы в FAQ'

    def __unicode__(self):
        return self.title


class AnswerFaq(models.Model):
    account = models.ForeignKey(Account)
    answer = models.TextField(verbose_name=u'Ответ на вопрос в FAQ')
    question = models.ForeignKey(QuestionFaq)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = u'Ответ на вопрос в FAQ'
        verbose_name_plural = u'Ответы на вопросы в FAQ'

    def __unicode__(self):
        return u'%s - вопрос: "%s"' % (
            self.account.get_full_name(),
            self.question.title)
