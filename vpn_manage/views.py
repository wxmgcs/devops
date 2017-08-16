# coding: utf8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse


def edit(request):
    return render(request,"vpn_manage.html")


def add(request):
    return render(request,"vpn_manage.html")


def delete(request):
    return render(request,"vpn_manage.html")


def list(request):
    return render(request,"vpn_manage.html")