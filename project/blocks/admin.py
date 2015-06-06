#-*- coding: utf-8 -*-
from django.contrib import admin
from models import IndexBlock


class IndexBlockAdmin(admin.ModelAdmin):
    model = IndexBlock
    list_display = ('name', 'id', 'link')
    fields = ('name', 'content', 'description', 'link')

admin.site.register(IndexBlock, IndexBlockAdmin)
