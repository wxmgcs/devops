#coding: utf-8
from django import forms
from .models import *


ALLOW_CHOICE = (
    (1, u'使用中'),
    (0, u'已过期')
)


class VPNForm(forms.ModelForm):
    class Meta:
        model = VPN
        fields = '__all__'
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'输入VPN账户'}),
            'pwd': forms.TextInput(attrs={'class': 'form-control','placeholder':'输入VPN密码'}),
            'status': forms.RadioSelect(choices=ALLOW_CHOICE, attrs={'class': 'flat'})
        }
