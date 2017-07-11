#!/usr/bin/env python
# coding: utf8
'''
@author: qitan
@contact: qqing_lai@hotmail.com
@file: forms.py
@time: 2017/3/30 15:34
@desc:
'''

from django import forms
from asset.models import IdcAsset

class IdcAssetForm(forms.ModelForm):
    class Meta:
        model = IdcAsset
        fields = ('idc_name', 'idc_type', 'idc_location', 'contract_date', 'idc_contacts', 'remark')
        widgets = {
          'idc_name': forms.TextInput(attrs={'class': 'form-control'}),
          'idc_type': forms.TextInput(attrs={'class': 'form-control'}),
          'idc_location': forms.TextInput(attrs={'class': 'form-control'}),
          'contract_date': forms.TextInput(attrs={'class': 'form-control'}),
          'idc_contacts': forms.TextInput(attrs={'class': 'form-control'}),
          'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }
