# coding: utf8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from  deploy.saltapi import SaltAPI
from devops import settings

def show_logger(request,id=None):

    if id:
        sapi = SaltAPI(url=settings.SALT_API['url'],username=settings.SALT_API['user'],password=settings.SALT_API['password'])
        # print sapi.list_all_key()
    return render(request,"logger_manage.html")