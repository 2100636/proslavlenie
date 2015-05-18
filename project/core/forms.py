# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Form
from project.core.models import Need
# from models import *


class NeedForm(forms.ModelForm):
    class Meta:
        model = Need


# class ProductFormCustom(forms.Form):
#     field1 = forms.CharField()
#     field2 = forms.IntegerField()
#

