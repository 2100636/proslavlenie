# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.contrib import admin
from models import BibleScool, HvalaScool, PenuelConf, Play2017


#
class BibleScoolAdmin(admin.ModelAdmin):
    model = BibleScool
    list_display = ('fio', 'city', 'phone' , 'date')
    list_display_links = ('fio',)
    list_per_page = 100

class HvalaScoolAdmin(admin.ModelAdmin):
    model = HvalaScool
    list_display = ('fi', 'date')
    list_display_links = ('fi',)
    list_per_page = 50


class PenuelConfAdmin(admin.ModelAdmin):
    model = PenuelConf
    list_display = ('fio', 'date')
    list_display_links = ('fio',)
    list_per_page = 50


admin.site.register(BibleScool, BibleScoolAdmin)
admin.site.register(HvalaScool, HvalaScoolAdmin)
admin.site.register(PenuelConf, PenuelConfAdmin)
admin.site.register(Play2017)
