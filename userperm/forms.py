#!/usr/bin/env python
# coding: utf8
'''
@author: qitan
@contact: qqing_lai@hotmail.com
@file: forms.py
@time: 2017/3/30 16:05
@desc:
'''

from django import forms
from .models import *


ALLOW_CHOICE = (
    (True, u'启用'),
    (False, u'禁用')
)
class CommandForm(forms.ModelForm):
    class Meta:
        model = UserCommand
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'填写别名'}),
            'command': forms.TextInput(attrs={'class': 'tags form-control','id':'tags_add'}),
            'is_allow': forms.RadioSelect(choices=ALLOW_CHOICE, attrs={'class': 'flat'})
        }

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = UserDirectory
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'填写别名'}),
            'directory': forms.TextInput(attrs={'class': 'tags form-control','id':'tags_add'}),
            'is_allow': forms.RadioSelect(choices=ALLOW_CHOICE, attrs={'class': 'flat'})
        }
