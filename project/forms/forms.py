# -*- coding: utf-8 -*-
from django import forms
from project.forms.models import BibleScool, HvalaScool, PenuelConf

class PenuelConfForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PenuelConfForm, self).__init__(*args, **kwargs)

        self.fields['fio'].widget.attrs = {
            'placeholder': 'Ф.И.О',
            'class': 'form-control floating-label'}
        self.fields['fio'].label = ''

        self.fields['city'].widget.attrs = {
            'placeholder': 'Город проживания',
            'class': 'form-control floating-label'}
        self.fields['city'].label = ''

        self.fields['phone'].widget.attrs = {
            'placeholder': 'Контактный телефон',
            'class': 'form-control floating-label'}
        self.fields['phone'].label = ''

        self.fields['email'].widget.attrs = {
            'placeholder': 'E-mail',
            'class': 'form-control floating-label'}
        self.fields['email'].label = ''

        self.fields['you_church'].widget.attrs = {
            'placeholder': 'К какой Церкви Вы принадлежите',
            'class': 'form-control floating-label'}
        self.fields['you_church'].label = ''

        self.fields['you_sluzhenie'].widget.attrs = {
            'placeholder': 'Ваше служение',
            'class': 'form-control floating-label'}
        self.fields['you_sluzhenie'].label = ''

    class Meta:
        model = PenuelConf
        exclude = ()




class BSForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BSForm, self).__init__(*args, **kwargs)

        self.fields['fio'].widget.attrs = {
            'placeholder': 'Ф.И.О',
            'class': 'form-control floating-label'}
        self.fields['fio'].label = ''

        self.fields['birth_day'].widget.attrs = {
            'placeholder': 'Дата рождения',
            'class': 'form-control floating-label'}
        self.fields['birth_day'].label = ''

        self.fields['phone'].widget.attrs = {
            'placeholder': 'Контактный телефон',
            'class': 'form-control floating-label'}
        self.fields['phone'].label = ''

        self.fields['city'].widget.attrs = {
            'placeholder': 'Город проживания',
            'class': 'form-control floating-label'}
        self.fields['city'].label = ''

        self.fields['family_status'].widget.attrs = {
            'placeholder': 'Семейное положение',
            'class': 'form-control floating-label'}
        self.fields['family_status'].label = ''

        self.fields['you_church'].widget.attrs = {
            'placeholder': 'К какой Церкви Вы принадлежите',
            'class': 'form-control floating-label'}
        self.fields['you_church'].label = ''

        self.fields['church_city'].widget.attrs = {
            'placeholder': 'Город',
            'class': 'form-control floating-label'}
        self.fields['church_city'].label = ''

        self.fields['pastor_fio'].widget.attrs = {
            'placeholder': 'Ф.И.О пастора Церкви',
            'class': 'form-control floating-label'}
        self.fields['pastor_fio'].label = ''

        # self.fields['is_church_member'].widget.attrs = {
        #     'placeholder': 'Являетесь ли Вы членом Церкви',
        #     'class': 'form-control floating-label'}
        # self.fields['is_church_member'].label = 'Являетесь ли Вы членом Церкви'

        self.fields['salvation_day'].widget.attrs = {
            'placeholder': 'Дата Вашего спасения',
            'class': 'form-control floating-label'}
        self.fields['salvation_day'].label = ''

        self.fields['you_mission'].widget.attrs = {
            'placeholder': 'Чувствуете ли Вы ясное призвание от Бога на служение? Если да, то какое?',
            'class': 'form-control floating-label'}
        self.fields['you_mission'].label = ''

    class Meta:
        model = BibleScool
        exclude = ()



class HvalaSForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HvalaSForm, self).__init__(*args, **kwargs)

        # self.fields['fi'].widget.attrs = {
        #     'placeholder': 'Ф.И',
        #     'class': 'form-control floating-label'}
        # self.fields['fi'].label = ''

        for field in self.fields:
            self.fields[field].widget.attrs = {'placeholder': self.fields[field].label, 'class': 'form-control floating-label'}
            if field != 'how_class':
                self.fields[field].label = ''
    class Meta:
        model = HvalaScool
        exclude = ()
