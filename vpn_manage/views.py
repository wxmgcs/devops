# coding: utf8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from vpn_manage.models import  VPN
from vpn_manage.forms import  VPNForm
import json

def edit(request,id=None):
    if request.user.is_superuser:
        action = ''
        page_name = ''

        print (id)
        if id:
            vpn = get_object_or_404(VPN, pk=id)
            action = 'edit'
            page_name = '编辑'
        else:
            vpn = VPN()
            action = 'add'
            page_name = '新增'

        if request.method == 'POST':
            print "post >> ",request.POST
            form = VPNForm(request.POST, instance=vpn)
            print form
            if form.is_valid():
                if action == 'add':
                    vpn = form.save(commit=False)
                else:
                    form.save
                vpn.save()
                return redirect('vpn_list')
            else:
                print ("invalid form >>>",form)
                return redirect('vpn_list')
        else:
            form = VPNForm(instance=vpn)
            return render(request, 'vpn_edit.html', {
            'form': form, 'action': action})
    else:
        print (">>>> not find vpn manage page")
        raise Http404


def delete(request,id=None):
    if request.user.is_superuser:
        vpn = get_object_or_404(VPN, pk=id)
        try:
            vpn.delete()
            return redirect('vpn_list')
        except Exception,ex:
            raise Http404
    else:
        raise Http404

def list(request):
    vpns = VPN.objects.filter()
    return render(request,"vpn_manage.html",{'vpns':vpns})

def get_config(request):
    if request.method == "GET":
        args = request.GET
        area_ip = args['ip']
        print area_ip
        try:
            vpn_obj = VPN.objects.get(area_ip=area_ip)
            print "vpn_obj >> ",vpn_obj
            vpn_username = vpn_obj.user_name
            print (vpn_username)
            pwd = vpn_obj.pwd
            remote_ip = vpn_obj.remote_ip
            status = vpn_obj.status
            return HttpResponse(json.dumps(dict(result=1,data=[dict(vpn_username=vpn_username,
                                                                    vpn_pwd=pwd,
                                                                    remote_ip=remote_ip,
                                                                    areaip=area_ip,
                                                                    status=status,
                                                                    id = vpn_obj.id
                                                                    )])))
        except Exception,ex:
            return HttpResponse(json.dumps(dict(result=2,reason=str(ex))))
    else:
        return HttpResponse(json.dumps(dict(result=3,reason="not support post method")))


