from django.test import TestCase
from devops import settings
from  deploy.saltapi import SaltAPI

sapi = SaltAPI(url=settings.SALT_API['url'],username=settings.SALT_API['user'],password=settings.SALT_API['password'])

def test_sapi():

    jid =  sapi.remote_execution('unicomrecharge_server6.ctu.com','cmd.run','cd c:\\salt\\bin & python c:\\UnicomRechargeV2/logger.py -c cat_log -eid E_1 -st "2017-08-25 09:50" -et "2017-08-25 10:46" -l 50','list')

def get_jid_info():
    print (sapi.salt_runner('20170825155400373754'))






# test_sapi()
get_jid_info()