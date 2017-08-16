from django.shortcuts import render
from django.http import Http404, HttpResponse
# Create your views here.
import json




def upload_genorder_result(request):
    ret = []
    if request.method == 'POST':
        print request.POST
        return HttpResponse(json.dumps(dict(result=0)))
    elif request.method == 'GET':
        return HttpResponse("ok")
    else:
        raise Http404


def control_board(request):
    
    
    
    return render(request, 'control_board.html')
