# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'project.faq.views',

    url(r'^faq/$', 'faqView',
        {'template_name': 'faq/faq.html'},
        name='faqView'),

    # api for faq
    url(r'^faq-tree/$', 'getFaqTree', name='faq-tree'),
    url(r'^post-answer/$', 'postAnswer', name='post-answer'),
    url(r'^post-question/$', 'postQuestion', name='post-question'),
    url(r'^user/$', 'getUser', name='get-user'),
    url(r'^post-question-checked/$', 'postQuestionChecked', name='post-question-checked')

)
