# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url
from views import NoticeFormView, CheckOrderFormView


urlpatterns = patterns('',
    url(r'^confirm-payment/$', 'project.payment.views.confirmFormView',
        {'template_name': 'confirm.html'},
        name='yandex_money_confirm'),

    url(r'^check/$', CheckOrderFormView.as_view(), name='yandex_money_check'),
    url(r'^aviso/$', NoticeFormView.as_view(), name='yandex_money_notice'),
)
