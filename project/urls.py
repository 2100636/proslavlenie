from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^', include('project.core.urls')),
    url(r'^', include('project.faq.urls')),
    url(r'^profile/', include('project.accounts.urls')),
    url(r'^api/v1/', include('project.faq.urls', namespace='faq_rest')),

    url(r'^fail-payment/$', TemplateView.as_view(template_name='fail.html'), name='payment_fail'),
    url(r'^success-payment/$', TemplateView.as_view(template_name='success.html'), name='payment_success'),
    url(r'^yandex-money/', include('project.payment.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
        # if work then show 404 Directory indexes are not allowed here.
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
        )
