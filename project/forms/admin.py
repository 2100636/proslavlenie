# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.contrib import admin
from models import BibleScool, HvalaScool



class HvalaScoolAdmin(admin.ModelAdmin):
    model = HvalaScool
    list_display = ('fi', 'date')
    list_display_links = ('fi',)
    list_per_page = 50

admin.site.register(BibleScool)
admin.site.register(HvalaScool, HvalaScoolAdmin)
