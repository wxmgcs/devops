# coding: utf8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from  deploy.saltapi import SaltAPI
from devops import settings
from deploy.models import  SaltHost
from program_manage.models import Program

import time
import datetime

def get_datetime():
    return time.strftime("%Y-%m-%d %H:%m", time.localtime())

def get_datetime_passed(day,minutes):
    return (datetime.datetime.now() - datetime.timedelta(days = day,minutes = minutes)).strftime("%Y-%m-%d %H:%M")


def get_log(hostname,program_id,start_time,end_time,lines):
    print (hostname,program_id,start_time,end_time,lines)

    sapi = SaltAPI(url=settings.SALT_API['url'],username=settings.SALT_API['user'],password=settings.SALT_API['password'])

    tgt = hostname
    if hostname == '0':
        tgt = '*'

    fun = "cmd.run"

    projectdir = settings.PROJECT_UNICOMRECHARGE['projectdir_windows']
    saltdir_windows = settings.PROJECT_UNICOMRECHARGE['saltdir_windows']

    arg = "cd %s & python %s\\manage.py cat_log %s start_time=%s end_time=%s lines=%s"%(saltdir_windows,projectdir,program_id,start_time,end_time,lines)
    expr_form = ""

    ret = sapi.remote_localexec(tgt,fun,arg,expr_form)
    if ret == {}:
        ret = "没有查询到结果"

    return ret

def list(request):
    log = []
    if request.method == 'GET':
        minions = SaltHost.objects.filter(status=True)
        programs = Program.objects.filter()
        print (minions,programs)
        start_time = get_datetime_passed(0,10)
        end_time = get_datetime()

        return render(request,"logger_manage.html",{'page_name':u"查看日志",
                                                    'query_button':u"查询",
                                                    'log':log,
                                                    'all_minions':minions,
                                                    'programs':programs,
                                                    'hostname':'',
                                                    'program_id':'0',
                                                    'lines':'',
                                                    'start_time':start_time,
                                                    'end_time':end_time,

                                                    })
    elif request.method == 'POST':
        post_args = request.POST
        print (post_args)

        hostname = post_args['host']
        program_id = post_args['program_id']
        lines = post_args['lines']
        start_time = post_args['start_time']
        end_time = post_args['end_time']

        log = get_log(hostname=hostname,program_id=program_id,start_time=start_time,end_time=end_time,lines=lines)

        minions = SaltHost.objects.filter(status=True)

        return render(request,"logger_manage.html",{'page_name':u"查看日志",
                                                    'query_button':"查询",
                                                    'log_content':log,
                                                    'all_minions':minions,
                                                    'hostname':hostname,
                                                    'program_id':program_id,
                                                    'lines':lines,
                                                    'start_time':start_time,
                                                    'end_time':end_time,
                                                    })

def show_logger(request,id=None):

    if id:
        sapi = SaltAPI(url=settings.SALT_API['url'],username=settings.SALT_API['user'],password=settings.SALT_API['password'])
        # print sapi.list_all_key()
    return render(request,"logger_manage.html",{'page_name':u"查看日志"})