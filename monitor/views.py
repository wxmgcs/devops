from django.shortcuts import render
from django.http import Http404, HttpResponse
# Create your views here.
import json
from .models import  UnicomRechargeGenOrder
import mysql_controller
from vpn_manage.models import VPN

def upload_genorder(request):
    if request.method == 'POST':
        data = json.loads(request.POST['genorder'])
        vpn_code = request.POST['vpn_code']
        keys = data.keys()
        for key in keys:
            vals = data.get(key)
            for item in vals:
                print (item['status'],item['create_time'])
                status = item['status']
                create_time = item['create_time']
                UnicomRechargeGenOrder.objects.create(eid=key,status=status,create_time=create_time,vpn_code=vpn_code)
        return HttpResponse(json.dumps(dict(result=0)))
    elif request.method == 'GET':
        return HttpResponse(json.dumps(dict(result=0)))
    else:
        raise Http404


def control_board(request):
    return render(request, 'control_board.html')

def statics_vpn_status(request):
    if request.method == "POST":
        data = request.POST
        minute = data['min']
        try:
            int(minute)
        except Exception,ex:
            return HttpResponse(json.dumps(dict(result=0,reason=str(ex))))
        return HttpResponse(json.dumps(dict(result=1,data=mysql_controller.get_genorder_status(minute))))
    else:
        return HttpResponse(json.dumps(dict(result=0,reason="not support")))

def get_fixed_vpn(request):
    if request.method == "POST":
        data = request.POST
        minute = data['min']
        try:
            int(minute)
        except Exception,ex:
            return HttpResponse(json.dumps(dict(result=0,reason=str(ex))))
        ret = mysql_controller.get_genorder_status(minute)
        vpns = VPN.objects.filter(status=1)
        vpn_size = len(vpns)
        if vpn_size == len(ret):
            return HttpResponse(json.dumps(dict(result=1,data=[])))
        result = []
        ids = vpns.values('id')
        ids = [int(item['id']) for item in ids]
        vpn_codes = [item['vpn_code'] for item in ret]
        for id in ids:
            if id not in vpn_codes:
                result.append(id)
        return HttpResponse(json.dumps(dict(result=1,data=result)))
    else:
        return HttpResponse(json.dumps(dict(result=0,reason="not support",data=[])))








