#!/usr/bin/env python
# coding: utf8
'''
@author: qitan
@contact: qqing_lai@hotmail.com
@file: views.py.py
@time: 2017/3/30 16:07
@desc:
'''

import functools
import warnings

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
)
from django.utils.deprecation import (
    RemovedInDjango20Warning, RemovedInDjango110Warning,
)
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.shortcuts import resolve_url
from django.utils.http import is_safe_url
from django.conf import settings as djsettings

from models import User, UserGroup

from deploy.models import SaltGroup
from userperm.views import UserIP
from userperm.models import Message

import json
import StringIO
from .forms import *


def deprecate_current_app(func):
    """
    Handle deprecation of the current_app parameter of the views.
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if 'current_app' in kwargs:
            warnings.warn(
                "Passing `current_app` as a keyword argument is deprecated. "
                "Instead the caller of `{0}` should set "
                "`request.current_app`.".format(func.__name__),
                RemovedInDjango20Warning
            )
            current_app = kwargs.pop('current_app')
            request = kwargs.get('request', None)
            if request and current_app is not None:
                request.current_app = current_app
        return func(*args, **kwargs)
    return inner



def  get_programlist():
    all_program = []
    # status = 1 '运行中', status = 0,已停止
    all_program.append(dict(pk=1,id='E_1',status=1,type=1,vpn_number=1,ip='192.168.3.31/211.111.222.333',os_type=1,operator=1))
    all_program.append(dict(pk=2,id='P_1',status=0,type=2,vpn_number=2,ip='192.168.3.32/211.111.222.334',os_type=2,operator=1))
    all_program.append(dict(pk=3,id='E_31',status=1,type=3,vpn_number=1,ip='192.168.3.33/211.111.222.335',os_type=1,operator=1))
    return all_program





@login_required
def index(request):
    '''
    获取服务器资产信息
    '''
    if request.method == 'GET':
        print "program list >>"," >> ",request.GET

        if request.user.has_perm('asset.view_asset'):
            ret = ''
            all_program = get_programlist()
            print request.GET
        else:
            raise Http404
        return render(request, 'program_list.html', {'all_program': all_program})
    elif request.method == 'POST':

        print "program list >>",request.method," >> ",request.POST
        # 处理根据哪些参数筛选程序名称
        post_args = request.POST
        filter = post_args['filter'][0]
        search_text = post_args['search_text']
        print search_text,filter

        all_program = get_programlist()

        if len(search_text) < 1:
            return render(request, 'program_list.html', {'all_program': all_program})

        search_text = search_text
        if search_text != '':
            all_program = filter_programs(filter,search_text,all_program)
        return render(request, 'program_list.html', {'all_program': all_program})


FILTER_PROGRAM_NUMBER="0"
FILTER_PROGRAM_STATUS="1"
FILTER_PROGRAM_TYPE = "2"
FILTER_SYSTEM_TYPE = "3"

# 根据查询条件筛选程序
def filter_programs(filter,search_text,all_programs):
    ret = []
    if filter == FILTER_PROGRAM_NUMBER:
        for item in all_programs:
            if item['id'] == search_text:
                ret.append(item)
        return ret
    elif filter == FILTER_PROGRAM_STATUS:
        for item in all_programs:
            if item['status'] == int(search_text):
                ret.append(item)
        return ret
    elif filter == FILTER_PROGRAM_TYPE:
        for item in all_programs:
            if item['type'] == int(search_text):
                ret.append(item)
        return ret
    elif filter == FILTER_SYSTEM_TYPE:
        if search_text.find("window") > -1:
            os_type = 1
        elif search_text.find("linux") > -1:
            os_type = 2
        else:
            os_type = 0
        for item in all_programs:
            if item['os_type'] == os_type:
                ret.append(item)
        return ret
    return ret

@deprecate_current_app
@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, redirect_field_name=REDIRECT_FIELD_NAME, authentication_form=AuthenticationForm):
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))
    if request.method == "POST":
        if request.POST.has_key('login'):
            form = authentication_form(request, data=request.POST)
            if form.is_valid():
                if form.get_user() and form.get_user().is_active:
                    # Ensure the user-originating redirection url is safe.
                    if not is_safe_url(url=redirect_to, host=request.get_host()):
                        redirect_to = resolve_url(djsettings.LOGIN_REDIRECT_URL)
                    auth_login(request, form.get_user())
                    Message.objects.create(type=u'用户登录', user=request.user, action=u'用户登录',
                                           action_ip=UserIP(request), content='用户登录 %s'%request.user)
                    return HttpResponseRedirect(redirect_to)
            else:
                Message.objects.create(type=u'用户登录', user=request.POST.get('username'), action=u'用户登录',
                                       action_ip=UserIP(request), content=u'用户登录失败 %s'%request.POST.get('username'))
    else:
        form = authentication_form(request)
    return render(request, 'registration/login.html', {'form':form, 'title':'用户登录'})

@deprecate_current_app
def logout(request, next_page=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    Message.objects.create(type=u'用户退出', user=request.user, action=u'用户退出', action_ip=UserIP(request),
                           content='用户退出 %s' % request.user)
    auth_logout(request)

    if next_page is not None:
        next_page = resolve_url(next_page)

    if (redirect_field_name in request.POST or
            redirect_field_name in request.GET):
        next_page = request.POST.get(redirect_field_name,
                                     request.GET.get(redirect_field_name))
        # Security check -- don't allow redirection to a different host.
        if not is_safe_url(url=next_page, host=request.get_host()):
            next_page = request.path

    if next_page:
        # Redirect to this page until the session has been cleared.
        return HttpResponseRedirect(next_page)

        return HttpResponseRedirect('/')

@login_required
def logoutw(request):
    Message.objects.create(type=u'用户退出', user=request.user, action=u'用户退出', action_ip=UserIP(request),content='用户退出 %s'%request.user)
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required
def user_list(request):
    all_users = User.objects.all()
    return render(request, 'userauth_user_list.html', {'all_users':all_users})

@login_required
def group_list(request):
    all_groups = UserGroup.objects.all()
    return render(request, 'userauth_group_list.html', {'all_groups':all_groups})

@login_required
def user_manage(request, aid=None, action=None):
    if request.user.has_perms(['asset.view_user', 'asset.edit_user']):
        page_name = ''
        if aid:
            user = get_object_or_404(User, pk=aid)
            if action == 'edit':
                page_name = '编辑用户'
            if action == 'delete':
                user.delete()
                Message.objects.create(type=u'用户管理', user=request.user.first_name, action=u'删除用户', action_ip=UserIP(request),
                                       content=u'删除用户 %s%s，用户名 %s' % (user.last_name, user.first_name, user.username))
                return redirect('user_list')
        else:
            user = User()
            action = 'add'
            page_name = '新增用户'

        if request.method == 'POST':
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                group_select = request.POST.getlist('group_sel')
                group_delete = request.POST.getlist('group_del')
                perm_select = request.POST.getlist('perm_sel')
                perm_delete = request.POST.getlist('perm_del')
                if action == 'add' or action == 'edit':
                    form.save
                    if password1 and password1 == password2:
                        user.set_password(password1)
                    user.save()
                    # 添加用户至UserGroup
                    user.group.add(*group_select)
                    user.group.remove(*group_delete)
                    # 添加用户至Group组，授权用户该组权限
                    user.groups.add(*group_select)
                    user.groups.remove(*group_delete)
                    # 授予用户权限
                    user.user_permissions.add(*perm_select)
                    user.user_permissions.remove(*perm_delete)
                    Message.objects.create(type=u'用户管理', user=request.user.first_name, action=page_name, action_ip=UserIP(request),
                                               content=u'%s %s%s，用户名 %s' % (
                                               page_name, user.last_name, user.first_name, user.username))
                    return redirect('user_list')
        else:
            form = UserForm(instance=user)

        return render(request, 'userauth_user_manage.html', {'form':form, 'page_name':page_name, 'action':action, 'aid':aid})
    else:
        raise Http404

@login_required
def group_manage(request, aid=None, action=None):
    if request.user.has_perms(['asset.view_user', 'asset.edit_user']):
        page_name = ''
        if aid and action:
            group = get_object_or_404(UserGroup, pk=aid)
            if action == 'edit':
                page_name = '编辑组'
            if action == 'delete':
                group.delete()
                Message.objects.create(type=u'用户分组管理', user=request.user.first_name, action=u'删除分组', action_ip=UserIP(request),
                                       content=u'删除分组 %s'%group.name)
                return redirect('user_group_list')
        else:
            group = UserGroup()
            action = 'add'
            page_name = '新增用户组'

        if request.method == 'POST':
            form = GroupForm(request.POST, instance=group)
            if form.is_valid():
                command_list = form.cleaned_data['command']
                directory_list = form.cleaned_data['directory']
                user_select = request.POST.getlist('user_sel')
                user_delete = request.POST.getlist('user_del')
                host_select = request.POST.getlist('host_sel')
                host_delete = request.POST.getlist('host_del')
                group_select = request.POST.getlist('group_sel')
                group_delete = request.POST.getlist('group_del')
                perm_select = request.POST.getlist('perm_sel')
                perm_delete = request.POST.getlist('perm_del')
                if action == 'add' or action == 'edit':
                    form.save
                    group.save()
                    group.user_group_set.add(*user_select)
                    group.user_group_set.remove(*user_delete)
                    group.user_set.add(*user_select)
                    group.user_set.remove(*user_delete)
                    group.host_usergroup_set.add(*host_select)
                    group.host_usergroup_set.remove(*host_delete)
                    group.group_usergroup_set.add(*group_select)
                    group.group_usergroup_set.remove(*group_delete)
                    group.permissions.add(*perm_select)
                    group.permissions.remove(*perm_delete)
                    if action == 'edit':
                        group.command.clear()
                        group.directory.clear()
                    group.command.add(*command_list)
                    group.directory.add(*directory_list)

                    Message.objects.create(type=u'用户分组管理', user=request.user.first_name, action=page_name, action_ip=UserIP(request),
                                               content=u'%s %s'%(page_name, group.name))
                    return redirect('user_group_list')
        else:
            form = GroupForm(instance=group)

        return render(request, 'userauth_group_manage.html', {'form':form, 'page_name':page_name, 'action':action, 'aid':aid})
    else:
        raise Http404

@login_required
def ajax_user_groups(request):
    user_groups = {i['pk']: i['group_name'] for i in
                   User.objects.get(pk=request.user.pk).group.values('pk', 'group_name')}

    return HttpResponse(json.dumps(user_groups))
