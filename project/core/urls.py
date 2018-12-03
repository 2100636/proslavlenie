# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'project.core.views',

    url(r'^crossdomain\.xml$', 'crossdomain_xmlView', {'template_name': 'core/crossdomain.html'}, name='crossdomain_xml'),

    url(r'^$', 'indexView',
        {'template_name': 'core/index.html'},
        name='indexView'),

    url(r'^articles/(?P<slug>[-\w]+)/$', 'articleView',
        {'template_name': 'core/article.html'},
        name='articleView'),

    url(r'^news/$', 'newsAllView',
        {'template_name': 'core/news_all.html'},
        name='newsAllView'),

    url(r'^news/(?P<id>[-\w]+)/$', 'newsView',
        {'template_name': 'core/news.html'},
        name='newsView'),

    url(r'^reviews/$', 'reviewsView',
        {'template_name': 'core/reviews.html'},
        name='reviewsView'),

    url(r'^review/(?P<id>[-\w]+)/$', 'reviewView',
        {'template_name': 'core/review.html'},
        name='reviewView'),

    url(r'^testimonys/$', 'testimonysView',
        {'template_name': 'core/testimonys.html'},
        name='testimonysView'),

    url(r'^testimony/(?P<id>[-\w]+)/$', 'testimonyView',
        {'template_name': 'core/testimony.html'},
        name='testimonyView'),

    url(r'^ministry/(?P<slug>[-\w]+)/$', 'ministryView',
        {'template_name': 'core/ministry.html'},
        name='ministryView'),

    url(r'^page/(?P<slug>[-\w]+)/$', 'pageView',
        {'template_name': 'core/page.html'},
        name='pageView'),

    url(r'^questions/$', 'questionsView',
        {'template_name': 'core/questions.html'},
        name='questionsView'),


    url(r'^adverts/add/$', 'advertAddView',
        {'template_name': 'core/advert_add.html'},
        name='advertAddView'),

    url(r'^adverts/deleteold/$', 'advertDeleteOldView',
        {'template_name': 'core/advert_delete_old.html'},
        name='advertDeleteOldView'),

    url(r'^adverts/(?P<category_slug>[-\w]+)$', 'advertCatView',
        {'template_name': 'core/advert_cat.html'},
        name='advertCatView'),

    url(r'^adverts/$', 'advertAllView',
        {'template_name': 'core/advert_all.html'},
        name='advertAllView'),
    
    url(r'^advert/(?P<slug>[-\w]+)/delete/$', 'advertDeleteView',
        {'template_name': 'core/advert_delete.html'},
        name='advertDeleteView'),

    url(r'^advert/(?P<slug>[-\w]+)/$', 'advertView',
        {'template_name': 'core/advert.html'},
        name='advertView'),
)
