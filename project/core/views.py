# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from functions import *
from forms import QuestionForm, NeedForm, AdvertForm
from project.forms.forms import BSForm, HvalaSForm, PenuelConfForm, Play2017Form
from models import Article, Page, Question,\
    News, SliderItem, Review, Testimony, Video, Ministry, VideoCategory, Advert, AdvertCategory, ProjectCategory, Project

from django.core.mail import send_mail
from project.settings import ADMIN_EMAIL, DEFAULT_FROM_EMAIL

from project.payment.forms import PaymentForm
from project.payment.models import Payment
import requests 
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math
from datetime import datetime, timedelta

def youtube_verificate_View(request):
    html = "google-site-verification: google211a33f553b0112c.html"
    return HttpResponse(html)

def crossdomain_xmlView(request, template_name="core/crossdomain.html"):
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request), content_type='application/xml')


def indexView(request, template_name="catalog/index.html"):
    user = request.user
    articles = Article.objects.order_by('-id')[:4]
    news = News.objects.order_by("-date")[:5]
    slides = SliderItem.objects.all()[:3]

    # получение ссылок для видео
    cat = VideoCategory.objects.all()
    for c in cat:
        if c.slug == 'main':
            main_video = Video.objects.filter(category=c).last()
            main_video.video = main_video.video[17:]
        elif c.slug == 'pritch':
            pritch_video = Video.objects.filter(category=c).last()
            pritch_video.video = pritch_video.video[17:]
        else:
            videoblog_video = Video.objects.filter(category=c).last()
            videoblog_video.video = videoblog_video.video[17:]

    reviews = Review.objects.order_by("-date")[:3]

    form_question = QuestionForm()
    form_need = NeedForm()

    # Отправляем на почту
    if request.method == "POST" and "need" in request.POST:
        form_need = NeedForm(request.POST)
        if form_need.is_valid():
            if request.POST.get('agreement', False) == False:
                form_msg = ['Ошибка заполнения формы "Молитвенная нужда"<br> Вы должны согласиться с пользовательским соглашением', '#DC7373']
            elif request.POST['e_mail'] != '':
                form_msg = ['Ошибка заполнения формы "Молитвенная нужда"<br> Обнаружен спам, попробуйте еще раз или позднее', '#DC7373']
            else:
                form_need.save()
                ## subject = u'Нужда proslavlenie.ru'
                ## message = u'телефон: %s \n Имя: %s \n Сообщение: %s \n почта: %s'\
                ##     % (
                ##         request.POST['phone'],
                ##         request.POST['name'],
                ##         request.POST['text'],
                ##         request.POST['email'])
                ## 
                ## send_mail(
                ##     subject, message, DEFAULT_FROM_EMAIL, [ADMIN_EMAIL, 'alena.keller2017@yandex.ru', 'flame_of_praise@mail.ru', 'elena.bmh@yandex.ru', '2100636@mail.ru'],
                ##     fail_silently=False)

                form_msg = ['Спасибо! Молитвенная просьба успешно отправлена', '#0773bb']
        else:
            form_msg = ['Ошибка заполнения формы <br> Проверьте корректность всех данных', '#DC7373']

    # Отправляем вопрос на почту
    elif request.method == "POST" and "question" in request.POST:
        ## postdata = {
        ##     'name': request.POST['name'],
        ##     'phone': request.POST['phone'],
        ##     'email': request.POST['email'],
        ##     'text': request.POST['text']
        ## }
        ## form_question = QuestionForm(postdata)
        form_question = QuestionForm(request.POST)
        if form_question.is_valid():
            if request.POST.get('agreement', False) == False:
                form_msg = ['Ошибка заполнения формы "Задать вопрос"<br> Вы должны согласиться с пользовательским соглашением', '#DC7373']
            elif request.POST['e_mail'] != '':
                form_msg = ['Ошибка заполнения формы "Задать вопрос"<br> Обнаружен спам, попробуйте еще раз или позднее', '#DC7373']
            else:
                form_question.save()

                ## subject = u'Вопрос proslavlenie.ru'
                ## message = u'телефон: %s \n Имя: %s \n Сообщение: %s \n'\
                ##     % (
                ##         request.POST['phone'],
                ##         request.POST['name'],
                ##         request.POST['email'],
                ##         request.POST['text']
                ##     )
    
                ## send_mail(
                ##    subject, message, DEFAULT_FROM_EMAIL, [ADMIN_EMAIL], fail_silently=False)
                ### r = requests.get("http://form.proslavlenie.ru/actions.php")

                form_msg = ['Спасибо! Вопрос успешно отправлен', '#0773bb']
        else:
            form_msg = ['Ошибка заполнения формы "Задать вопрос"<br> Проверьте корректность всех данных', '#DC7373']
    

    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def articleView(request, slug, template_name="catalog/article.html"):
    user = request.user
    article = Article.objects.get(slug=slug)
    # мета описание
    meta_title = article.meta_title
    if not meta_title or meta_title == '':
        meta_title = article.name
    meta_description = article.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def newsView(request, id, template_name="catalog/news.html"):

    if request.path_info == '/news/141/':
        form = PenuelConfForm()

    if request.method == 'POST' and 'PenuelConfForm' in request.POST:
        form = PenuelConfForm(request.POST)
        if form.is_valid():
            form.save()
            subject = u'Анкета для конференции Пенуэл в Томске'
            message = u'ФИО: %s \n Город: %s \n Телефон: %s \n E-mail: %s \n Название церкви: %s \n ' \
                      u'Служение: %s \n '\
                % (
                    request.POST['fio'],
                    request.POST['city'],
                    request.POST['phone'],
                    request.POST['email'],
                    request.POST['you_church'],
                    request.POST['you_sluzhenie'],
                    )
            send_mail(
                subject, message, DEFAULT_FROM_EMAIL, [ADMIN_EMAIL], fail_silently=False)
                #subject, message, DEFAULT_FROM_EMAIL, ['2100636@mail.ru'], fail_silently=False)
            form_msg = ['Спасибо за регистрацию! <br> В ближайшее время с вами свяжутся для подтверждения регистрации.', '#0773bb']
        else:
            form_msg = ['Ошибка заполнения анкеты. Проверьте корректность всех данных', '#DC7373']


    if request.path_info == '/news/109/':
        form = HvalaSForm()

    if request.method == 'POST' and 'hvalas_form' in request.POST:
        form = HvalaSForm(request.POST)
        if form.is_valid():
            if request.POST.get('agreement', False) == False:
                form_msg = ['Ошибка заполнения анкеты <br> Вы должны согласиться с пользовательским соглашением', '#DC7373']
            else:
                form.save()
                subject = u'Анкета для поступления в Школу Хвалы'
                message = u'ФИ: %s \n Город, название церкцви: %s \n телефон: %s \n Возраст: %s \n ' \
                          u'Музыкальное образование: %s \n Класс обучения: %s \n Применять в: %s \n ' \
                          u'ФИ лидера: %s '\
                          u'Согласен с пользовательским соглашением: да' \
                    % (
                        request.POST['fi'],
                        request.POST['city'],
                        request.POST['phone'],
                        request.POST['age'],
                        request.POST['music_education'],
                        request.POST['how_class'],
                        request.POST['type_ministry'],
                        request.POST['leader_fi']
                        )

                send_mail(
                    subject, message, DEFAULT_FROM_EMAIL, [ADMIN_EMAIL], fail_silently=False)
                    #subject, message, DEFAULT_FROM_EMAIL, ['2100636@mail.ru'], fail_silently=False)

                form_msg = ['Спасибо! Анкета успешно отправлена', '#0773bb']
        else:
            form_msg = ['Ошибка заполнения анкеты. Проверьте корректность всех данных', '#DC7373']

    user = request.user
    news = News.objects.get(id=id)
    # мета описание
    meta_title = news.meta_title
    if not meta_title or meta_title == '':
        meta_title = news.name
    meta_description = news.meta_description
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def newsAllView(request, template_name="catalog/news_all.html"):
    news_all = News.objects.order_by("-date")
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def reviewsView(request, template_name="catalog/reviews.html"):
    reviews = Review.objects.order_by("-date")
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def reviewView(request, id, template_name="catalog/review.html"):
    review = Review.objects.get(id=id)
    # мета описание
    meta_title = review.meta_title
    if not meta_title or meta_title == '':
        meta_title = review.name
    meta_description = review.meta_description
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def testimonysView(request, template_name="catalog/reviews.html"):
    testimonys = Testimony.objects.all().order_by('-id')
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def testimonyView(request, id, template_name="catalog/testimony.html"):
    user = request.user
    testimony = Testimony.objects.get(id=id)
    # мета описание
    meta_title = testimony.meta_title
    if not meta_title or meta_title == '':
        meta_title = testimony.name
    meta_description = testimony.meta_description
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def ministryView(request, slug, template_name="core/ministry.html"):

    if request.path_info == '/ministry/biblejskie-kursy/':
        template_name="core/ministry_biblejskie_kursy.html"
        form = BSForm()

    if request.method == 'POST' and 'bs_form' in request.POST:
        form = BSForm(request.POST)
        if form.is_valid():
            if request.POST.get('agreement', False) == False:
                form_msg = ['Ошибка заполнения анкеты <br> Вы должны согласиться с пользовательским соглашением', '#DC7373']
            else:
                form.save()
                #subject = u'Анкета БШ'
                #message = u'ФИО: %s \n Дата рождения: %s \n телефон: %s \n город: %s \n Семейное положение: %s \n ' \
                #        u'Принадлежность к церкви: %s \n Город: %s \n Ф.И.О пастора Церкви: %s \n Член Церкви: %s \n ' \
                #        u'Верует ли в Господа: %s \n Дата спасения: %s \n Призвание: %s \n Форма обучения: %s \n ' \
                #        u'Согласен с правилами: %s \n Согласен с пользовательским соглашением: да' \
                #    % (
                #        request.POST['fio'],
                #        request.POST['birth_day'],
                #        request.POST['phone'],
                #        request.POST['city'],
                #        request.POST['family_status'],
                #        request.POST['you_church'],
                #        request.POST['church_city'],
                #        request.POST['pastor_fio'],
                #        request.POST.get('is_church_member', False),
                #        request.POST.get('is_believer', False),
                #        request.POST['salvation_day'],
                #        request.POST['you_mission'],
                #        request.POST['form_of_study'],
                #        request.POST.get('rules', False)
                #        )
#
                #send_mail(
                #    #subject, message, DEFAULT_FROM_EMAIL, ['bk.tomsk@mail.ru'], fail_silently=False)
                #    subject, message, DEFAULT_FROM_EMAIL, ['2100636@mail.ru'], fail_silently=False)
                form_msg = ['Спасибо! Анкета успешно отправлена', '#0773bb']
        else:
            form_msg = ['Ошибка заполнения анкеты <br> Проверьте корректность всех данных', '#DC7373']

    #######################

    if request.path_info == '/ministry/molodezhnoe-sluzhenie/':
        form = Play2017Form()

    if request.method == 'POST' and 'ms_form' in request.POST:
        form = Play2017Form(request.POST)
        if form.is_valid():
            if request.POST.get('agreement', False) == False:
                form_msg = ['Ошибка заполнения анкеты <br> Вы должны согласиться с пользовательским соглашением', '#DC7373']
            else:
                form.save()
                if request.POST['whoiam'] == '1':
                    whoiam = u'Молодежный пастор'
                elif request.POST['whoiam'] == '2':
                    whoiam = u'Подростковый пастор'
                elif request.POST['whoiam'] == '3':
                    whoiam = u'Молодежный лидер'
                elif request.POST['whoiam'] == '4':
                    whoiam = u'Подростковый лидер'
                elif request.POST['whoiam'] == '5':
                    whoiam = u'Прославление'
                elif request.POST['whoiam'] == '6':
                    whoiam = u'Администрирование'
                elif request.POST['whoiam'] == '7':
                    whoiam = u'Медиа'
                else:
                    whoiam = request.POST['whoiam_custom']
                subject = u'Анкета PLAY 2017'
                message = u'ФИО: %s \n Возраст (полных лет): %s \n Пол: %s \n Город: %s \n Название церкви: %s \n ' \
                        u'ФИО старшего пастора: %s \n Кем вы являетесь на данный момент: %s \n ' \
                        u'E-mail: %s \n ' \
                        u'Телефон: %s \n ' \
                        u'Согласен с пользовательским соглашением: да' \
                    % (
                        request.POST['fio'],
                        request.POST['age'],
                        request.POST['sex'],
                        request.POST['city'],
                        request.POST['you_church'],
                        request.POST['pastor_fio'],
                        whoiam,
                        request.POST['email'],
                        request.POST['phone'],
                        )

                send_mail(
                    subject, message, DEFAULT_FROM_EMAIL, ['youth_of_praise@mail.ru'], fail_silently=False)
                    #subject, message, DEFAULT_FROM_EMAIL, ['2100636@mail.ru'], fail_silently=False)
                form_msg = ['Спасибо! Анкета успешно отправлена', '#0773bb']
        else:
            form_msg = ['Ошибка заполнения анкеты <br> Проверьте корректность всех данных', '#DC7373']
    
    #######################

    user = request.user
    ministry = Ministry.objects.get(slug=slug)
    ministry.video = ministry.video[17:]
    # мета описание
    meta_title = ministry.meta_title
    if not meta_title or meta_title == '':
        meta_title = ministry.name
    meta_description = ministry.meta_description
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def pageView(request, slug, template_name="core/page.html"):
    page = Page.objects.get(slug=slug)
    # мета описание
    meta_title = page.meta_title
    if not meta_title or meta_title == '':
        meta_title = page.name
    meta_description = page.meta_description
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def questionsView(request, template_name="core/questions.html"):
    questions = Question.objects.all()
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))




def advertView(request, slug, template_name="catalog/advert.html"):
    user = request.user
    advert = Advert.objects.get(slug=slug)
    categories = AdvertCategory.objects.all()
    # мета описание
    # meta_title = advert.meta_title
    # if not meta_title or meta_title == '':
    #     meta_title = advert.name
    # meta_description = advert.meta_description
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def advertDeleteView(request, slug, template_name="catalog/advert.html"):
    user = request.user
    categories = AdvertCategory.objects.all()

    if request.method == "POST" and "pass" in request.POST and "id" in request.POST:
        if request.POST['pass'] != "":
            try:
                advert_to_del = Advert.objects.get(id=request.POST['id'], slug=slug,pswd=request.POST['pass'])
                Advert.objects.filter(id=request.POST['id'], slug=slug,pswd=request.POST['pass']).delete()
                status = 1;
            except Advert.DoesNotExist:
                status = 0;

    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def advertDeleteOldView(request, template_name="catalog/advert_delete_old.html"):
    categories = AdvertCategory.objects.all()
    c = Advert.objects.filter(date__lte=datetime.now()-timedelta(days=30)).delete()
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def advertCatView(request, category_slug, template_name="catalog/advert_cat.html"):
    categories = AdvertCategory.objects.all()
    category = AdvertCategory.objects.get(slug=category_slug)

    # количество объектов на странице
    objects_on_page = 20

    adverts = Advert.objects.filter(category=category.id,status=1).order_by("-id")
    paginator = Paginator(adverts, objects_on_page)
    pageNumber = request.GET.get('page')

    try: 
        paginatedPage = paginator.page(pageNumber)
    except PageNotAnInteger: 
        pageNumber = 1
    except EmptyPage: 
        pageNumber = paginator.num_pages
    adverts = paginator.page(pageNumber)

    pageNumber_ = int(pageNumber);

    count_page = adverts.paginator.count / objects_on_page
    ostatok = adverts.paginator.count % objects_on_page
    if ostatok != 0:
        count_page = count_page+1
    
    range_ = range(1, count_page+1)


    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


def advertAllView(request, template_name="catalog/advert_all.html"):
    categories = AdvertCategory.objects.all()

    # количество объектов на странице
    objects_on_page = 20

    adverts = Advert.objects.filter(status=1).order_by("-id")
    paginator = Paginator(adverts, objects_on_page)
    pageNumber = request.GET.get('page')

    try: 
        paginatedPage = paginator.page(pageNumber)
    except PageNotAnInteger: 
        pageNumber = 1
    except EmptyPage: 
        pageNumber = paginator.num_pages
    adverts = paginator.page(pageNumber)

    pageNumber_ = int(pageNumber);

    count_page = adverts.paginator.count / objects_on_page
    ostatok = adverts.paginator.count % objects_on_page
    if ostatok != 0:
        count_page = count_page+1
    
    range_ = range(1, count_page+1)

    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))



def advertAddView(request, template_name="catalog/advert_add.html"):
    categories = AdvertCategory.objects.all()
    form_advert = AdvertForm()

    if request.method == "POST" and "form_advert" in request.POST:

        if request.POST['e_mail'] != "":
            form_msg = ['Ошибка заполнения формы <br> Обнаружен спам.', '#DC7373']
            return render_to_response(
                template_name, locals(), context_instance=RequestContext(request))

        spam1 = re.findall(r'<a ', request.POST['text'])
        if spam1:
            form_msg = ['Ошибка заполнения формы <br> Обнаружен спам.', '#DC7373']
            return render_to_response(
                template_name, locals(), context_instance=RequestContext(request))

        form_advert = AdvertForm(request.POST, request.FILES)
        if form_advert.is_valid():
            form_advert.save()
            form_msg = ['Спасибо! Ваше объявление отправлено, после модерации оно будет опубликовано', '#0773bb']
            ### 
            ### post_data = request.POST
            ###
            ### response = requests.post('http://form.proslavlenie.ru/test.php', data=post_data)
            ### content = response.content            
        else:
            form_msg = ['Ошибка заполнения формы <br> Проверьте корректность всех данных', '#DC7373']

    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))







def partnershipView(request):
    categories = ProjectCategory.objects.all()

    # количество объектов на странице
    objects_on_page = 20

    projects = Project.objects.filter(status=1).order_by("-id")
    paginator = Paginator(projects, objects_on_page)
    pageNumber = request.GET.get('page')

    try: 
        paginatedPage = paginator.page(pageNumber)
    except PageNotAnInteger: 
        pageNumber = 1
    except EmptyPage: 
        pageNumber = paginator.num_pages
    projects = paginator.page(pageNumber)

    pageNumber_ = int(pageNumber);

    count_page = projects.paginator.count / objects_on_page
    ostatok = projects.paginator.count % objects_on_page
    if ostatok != 0:
        count_page = count_page+1
    
    range_ = range(1, count_page+1)

    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


