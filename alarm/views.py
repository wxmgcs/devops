# coding: utf8
from django.shortcuts import render,render_to_response

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse

from .models import Log
from .models import  Peer
import functools
import warnings
from django.contrib.auth.decorators import login_required
from program_manage import program_helper
import json
import time
from  alarm import email_helper

def get_datetime():
    return time.strftime("%Y-%m-%d %H:%m:%s", time.localtime())

def send_alarm(request):
    if request.method == 'POST':
        print (request.POST['data'])
        data = json.loads(request.POST['data'])
        title = data.get('title')
        content = data.get('content')
        peers = Peer.objects.filter(status=1)
        print (peers)
        for peer in peers:
            Log.objects.create(title=title,content=content,create_time=get_datetime(),peer=peer)
            email_helper.send_mail(title,content)
        return HttpResponse(json.dumps(dict(result=0)))
    elif request.method == 'GET':
        return HttpResponse("ok")
    else:
        raise Http404
