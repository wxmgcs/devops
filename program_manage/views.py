# coding: utf8
from django.shortcuts import render,render_to_response

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse

from program_manage.models import Program
from program_manage.forms import  ProgramForm
import functools
import warnings
from django.contrib.auth.decorators import login_required
from program_manage import program_helper

@login_required
def program_list(request):

    all_program = Program.objects.filter()
    print all_program

    #
    '''
    获取服务器资产信息
    '''
    if request.method == 'GET':
        print "program list >>"," >> ",request.GET

        if request.user.has_perm('asset.view_asset'):
            ret = ''
            print request.GET
        else:
            raise Http404
        return render(request, 'program_list.html', {'all_program': all_program,'program_id':''})
    elif request.method == 'POST':

        print "program list >>",request.method," >> ",request.POST
        # 处理根据哪些参数筛选程序名称
        post_args = request.POST

        filter = post_args['filter'][0]
        search_text = post_args['search_text']
        print search_text,filter

        all_program = Program.objects.filter()
        print all_program

        if len(search_text) < 1:
            return render(request, 'program_list.html', {'all_program': all_program,'program_id':''})

        search_text = search_text
        if search_text != '':
            all_program = filter_programs(filter,search_text,all_program)
        return render(request, 'program_list.html', {'all_program': all_program,'program_id':''})

# 新建程序
def add(request):
    print "program list >>",request.method," >> ",request.POST
    # 处理根据哪些参数筛选程序名称
    args = request.GET

    # 新建程序
    if 'new_program_name' in args:
        program_id = args['new_program_name']
        if program_id != '':
            try:
                Program.objects.create(program_id=program_id)
            except Exception,ex:
                print ex
                pass
    all_program = Program.objects.filter()
    return render_to_response('program_list.html', {'all_program': all_program,'program_id':''})


FILTER_PROGRAM_NUMBER="0"
FILTER_PROGRAM_STATUS="1"
FILTER_PROGRAM_TYPE = "2"
FILTER_SYSTEM_TYPE = "3"

def format_search_text(search_text):
    if search_text == "windows":
        search_text = 1
    elif search_text == "linux":
        search_text = 2
    elif search_text == u"下单":
        search_text = 1
    elif search_text == u"支付":
        search_text = 2
    elif search_text == u"核单":
        search_text = 3
    elif search_text == u"运行中":
        search_text = 1
    elif search_text == u"已停止":
        search_text = 0
    return search_text

# 根据查询条件筛选程序
def filter_programs(filter,search_text,all_programs):

    # search_text = format_search_text(search_text)
    ret = []
    if filter == FILTER_PROGRAM_NUMBER:
        for item in all_programs:
            if item.program_id == search_text:
                ret.append(item)
        return ret
    elif filter == FILTER_PROGRAM_STATUS:
        for item in all_programs:
            if item.status == search_text:
                ret.append(item)
        return ret
    elif filter == FILTER_PROGRAM_TYPE:
        for item in all_programs:
            if item.type == search_text:
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
            if item['os_type'] == search_text:
                ret.append(item)
        return ret
    return ret


@login_required
def program_edit(request,id=None):
    if request.user.is_superuser:
        action = ''
        page_name = ''
        print id
        if id:
            program = get_object_or_404(Program, pk=id)
            action = 'edit'
            page_name = '编辑程序'
        else:
            program = Program()
            action = 'add'
            page_name = '新增程序'

        # if request.method == 'GET':
        #     return redirect('program_list')

        if request.method == 'POST':
            form = ProgramForm(request.POST, instance=program)
            if form.is_valid():
                if action == 'add':
                    program = form.save(commit=False)
                else:
                    form.save
                program.save()

                return redirect('program_list')
            else:
                return redirect('program_list')

        else:
            form = ProgramForm(instance=program)

        return render(request, 'program_edit.html', {
            'form': form, 'action': action, 'page_name': page_name})
    else:
        raise Http404




def program_delete(request,id=None):
    if request.user.is_superuser:
        if id and request.method == 'GET':
            program = get_object_or_404(Program, pk=id)
            program.delete()
            all_program = Program.objects.filter()
            print (all_program)
            return redirect('program_list.html')
            # return render(request, 'program_list.html',{'all_program': all_program})
        else:
            return redirect('program_list.html')
            # return render(request, 'program_list.html',{'program_id':''})
    else:
        raise Http404




def program_stop(request,id=None):
    if request.user.is_superuser:
        if id and request.method == 'GET':
            program = get_object_or_404(Program, pk=id)
            nodename = program.nodename
            program_id = program.program_id
            tag = "stop"
            program_helper.run_cmd(nodename,program_id,tag)
            return HttpResponse("ok")
        else:
            return HttpResponse("error")
    else:
        raise Http404

def program_start(request,id=None):
    if request.user.is_superuser:
        if id and request.method == 'GET':
            program = get_object_or_404(Program, pk=id)
            nodename = program.nodename
            program_id = program.program_id
            tag = "start"
            program_helper.run_cmd(nodename,program_id,tag)
            return HttpResponse("ok")
        else:
            return HttpResponse("error")
    else:
        raise Http404

def program_restart(request,id=None):
    if request.user.is_superuser:
        if id and request.method == 'GET':
            program = get_object_or_404(Program, pk=id)
            nodename = program.nodename
            program_id = program.program_id
            tag = "restart"
            program_helper.run_cmd(nodename,program_id,tag)
            return HttpResponse("ok")
        else:
            return HttpResponse("error")
    else:
        raise Http404


def control_board(request):
    return redirect('control_board.html')