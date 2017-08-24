from django.test import TestCase

# Create your tests here.
#coding:utf-8

import time
import urllib2
import urllib
import json

def get_localtime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

order_list={}
order_key=[]
def statics(eid,stat):
    localtime = get_localtime()
    if eid not in order_key:
        order_key.append(eid)
        order_list.update({eid:[dict(create_time=localtime,status=stat)]})
    else:
        orderinfo = order_list.get(eid)
        orderinfo.append(dict(create_time=localtime,status=stat))
        order_list.update({eid:orderinfo})


statics("E_1","1")
statics("E_1","2")
statics("E_2","1")
statics("E_3","1")
statics("E_2","1")

def post(url,parameters):
    data = urllib.urlencode(parameters)
    print data
    request=urllib2.Request(url,data)
    return urllib2.urlopen(request).read()


def push_result():
    parameters = json.dumps(order_list)
    print parameters
    print
    parameters = {"genorder":parameters,"vpn_code":"1"}
    post("http://devops.ctu.com:9992/monitor/unicomrecharge/upload_genorder/",parameters)


print order_list,
print order_key
push_result()