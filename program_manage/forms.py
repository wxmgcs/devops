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
    (1, u'下单'),
    (2, u'支付'),
    (3, u'核单')
)

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        widgets = {
            'program_id': forms.TextInput(attrs={'class': 'form-control','placeholder':'输入程序编号'}),
            'program_type': forms.RadioSelect(choices=ALLOW_CHOICE, attrs={'class': 'flat'}),
        }
