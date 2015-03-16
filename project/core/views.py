# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.shortcuts import render
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.context_processors import csrf
from project.core.functions import *
from project.accounts.models import getOrganizerProfile
from project.accounts.forms import OrganizerProfileForm, UserRegistrationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from project.core.models import Article, ArticleGalleryImage, Page, PageGalleryImage, News, SliderItem, Review
from project.menu.models import MenuCategory


def indexView(request, template_name="catalog/index.html"):
    user = request.user
    articles = Article.objects.all()
    news = News.objects.all()[:5]
    menu_objects = MenuCategory.objects.all()
    slides = SliderItem.objects.all()[:3]
    # for slide in slides:
    #     try:
    #         slide.article = Article.objects.get(slider=slide.id)
    #     except:
    #         None
    reviews = Review.objects.all()[:2]


    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def articleView(request, slug, template_name="catalog/article.html"):
    user = request.user
    article = Article.objects.get(slug=slug)

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def newsView(request, id, template_name="catalog/news.html"):
    user = request.user
    news = News.objects.get(id=id)

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def reviewsView(request, template_name="catalog/reviews.html"):
    reviews = Review.objects.all()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))