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

# return Windows || CentOS
def get_os_type(saltapi,nodename):
    if nodename == '0':
        return None
    ret = saltapi.remote_localexec(nodename,"grains.item","os","list")
    return ret[nodename]['os']


def get_project_dir(os_type):
    if os_type == "Windows":
        return settings.PROJECT_UNICOMRECHARGE['projectdir_windows']
    elif os_type == "CentOS":
        return  settings.PROJECT_UNICOMRECHARGE['projectdir_linux']
    return None

def get_salt_dir(os_type):
    if os_type == "Windows":
        return settings.PROJECT_UNICOMRECHARGE['saltdir_windows']
    elif os_type == "CentOS":
        return settings.PROJECT_UNICOMRECHARGE['saltdir_linux']

def format_remote_exec(saltdir,projectdir,program_id,start_time,end_time,lines):
    return "cd %s & python %s/logger.py -c cat_log -eid %s -st %s -et %s -l %s"%(saltdir,projectdir,program_id,start_time,end_time,lines)


def format_loggerresult(result):
    logger = {}
    for key in result.keys():
        logger = result.get(key)
    return logger





def get_log(hostname,program_id,start_time,end_time,lines):
    ret = []

    sapi = SaltAPI(url=settings.SALT_API['url'],username=settings.SALT_API['user'],password=settings.SALT_API['password'])

    tgt = hostname
    if hostname == '0':
        tgt = '*'

    fun = "cmd.run"
    expr_form = "list"

    os_type  = get_os_type(sapi,hostname)
    start_time = "\""+start_time+"\""
    end_time = "\""+end_time+"\""

    if os_type is not None:
        # 查询全部的日志
        projectdir = get_project_dir(os_type)
        saltdir = get_salt_dir(os_type)

        arg = format_remote_exec(saltdir,projectdir,program_id,start_time,end_time,lines)
        result = sapi.remote_localexec(tgt,fun,arg,expr_form)
        result = format_loggerresult(result)
        ret.append(result)
    else:
        # windows
        tgt = "-G os:Windows"
        saltdir = settings.PROJECT_UNICOMRECHARGE['saltdir_windows']
        projectdir = settings.PROJECT_UNICOMRECHARGE['projectdir_windows']

        arg = format_remote_exec(saltdir,projectdir,program_id,start_time,end_time,lines)
        ret.append(sapi.remote_localexec(tgt,fun,arg,expr_form))

        tgt = "-G os:CentOS"
        saltdir = settings.PROJECT_UNICOMRECHARGE['saltdir_linux']
        projectdir = settings.PROJECT_UNICOMRECHARGE['projectdir_linux']
        arg = format_remote_exec(saltdir,projectdir,program_id,start_time,end_time,lines)
        ret.append(sapi.remote_localexec(tgt,fun,arg,expr_form))


    if ret == []:
        ret = "没有查询到结果"+get_datetime()

    ret = "\n".join(ret)
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