from django.shortcuts import render
from django.http import Http404, HttpResponse
# Create your views here.
import json
from .models import  UnicomRechargeGenOrder

def upload_genorder(request):
    if request.method == 'POST':
        print request.POST
        print request.POST
        data = json.loads(request.POST['genorder'])
        keys = data.keys()
        for key in keys:
            vals = data.get(key)
            for item in vals:
                print (item['status'],item['create_time'])
                status = item['status']
                create_time = item['create_time']
                UnicomRechargeGenOrder.objects.create(eid=key,status=status,create_time=create_time)
        return HttpResponse(json.dumps(dict(result=0)))
    elif request.method == 'GET':
        return HttpResponse("ok")
    else:
        raise Http404




def control_board(request):
    return render(request, 'control_board.html')
