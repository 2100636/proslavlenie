# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.template import RequestContext
from django.shortcuts import render_to_response
# from django.core.mail import send_mail
# from project.settings import ADMIN_EMAIL
# from django.views.decorators.csrf import csrf_protect
from models import QuestionFaq, AnswerFaq
from authentication.models import Account
from serializers import create_faq_tree
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
import json


def faqView(request, template_name="faq/faq.html"):

    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def getFaqTree(request):

    # все отзывы видит только зарегистрированный пользователь
    if request.method == 'GET' and request.user.is_authenticated() and request.user.is_servant:
        questions = QuestionFaq.objects.order_by("-date")
        tree = create_faq_tree(questions)
    elif request.method == 'GET' and not request.user.is_authenticated() or not request.user.is_servant:
        questions = QuestionFaq.objects.filter(checked=True).order_by("-date")
        tree = create_faq_tree(questions)

    return HttpResponse(tree, content_type="application/json")


def getUser(request):

    data = json.dumps({'username': 'anonimous'})
    if request.method == 'GET' and request.user.is_authenticated():
        data = json.dumps({
            'username': u"%s" % request.user.get_full_name(),
            'is_servant': request.user.is_servant
        })

    return HttpResponse(data, content_type="application/json")


@csrf_protect
def postAnswer(request):
    data = json.dumps({'message': "У Вас не достаточно прав."})

    if request.method == 'POST' and request.user.is_authenticated():
        id = request.POST['id']
        new_answer = AnswerFaq()
        new_answer.answer = request.POST['text']
        new_answer.account = request.user
        new_answer.question = QuestionFaq.objects.get(id=id)
        new_answer.save()

        data = json.dumps({
            'text': new_answer.answer,
            'question_id': id,
            'photo': "/media/%s" % new_answer.account.photo,
            'name': new_answer.account.get_full_name(),
            'date': "%s" % new_answer.date,
            'message': "Спасибо, Вы успешно добавили ответ на вопрос."
        })

    return HttpResponse(data, content_type="application/json")


@csrf_protect
def postQuestion(request):
    data = json.dumps({
        'message': "Извините, что-то пошло не так, попробуйте позже."})

    if request.method == 'POST' and request.POST['title'] == '' or request.POST['text'] == '':
        data = json.dumps({
            'message': "Необходимо заполнить все поля."})

    elif request.method == 'POST' and request.POST['title'] != '' or request.POST['text'] != '':
        new_question = QuestionFaq()
        new_question.title = request.POST['title']
        new_question.question = request.POST['text']
        new_question.save()

        data = json.dumps({
            'text': new_question.question,
            'question_id': new_question.id,
            'title': new_question.title,
            'date': "%s" % new_question.date,
            'answers': [],
            'message': "Спасибо, Вы успешно добавили вопрос."
        })

    return HttpResponse(data, content_type="application/json")


@csrf_protect
def postQuestionChecked(request):
    data = json.dumps({
        'message': "Извините, что-то пошло не так, попробуйте позже."})

    if request.method == 'POST' and request.POST['id']:
        id = int(request.POST['id'])
        question = QuestionFaq.objects.get(id=id)
        if request.POST['status'] == 'true':
            question.checked = True
        else: 
            question.checked = False
        question.save()

        data = json.dumps({
            'text': question.question,
            'question_id': question.id,
            'title': question.title,
            'date': "%s" % question.date,
            'answers': [],
            'message': "Спасибо, Вы успешно изменили статус вопроса."
        })

    return HttpResponse(data, content_type="application/json")

