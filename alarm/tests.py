from django.test import TestCase

# Create your tests here.
# Create your tests here.
import urllib
import urllib2
import json

def post(url,parameters):
    data = urllib.urlencode(parameters)
    print (data)
    request=urllib2.Request(url,data)
    return urllib2.urlopen(request).read()


def push_result(title,content):
    parameters = json.dumps(dict(title=title,content=content))
    print (parameters)
    parameters = {"data":parameters}
    post("http://localhost:9992/monitor/alarm/",parameters)

if __name__ == '__main__':
    push_result("[VPN] is distory","ip=xxxx")