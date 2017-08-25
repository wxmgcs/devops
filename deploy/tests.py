from django.test import TestCase

# Create your tests here.

from devops import settings
from  deploy.saltapi import SaltAPI

sapi = SaltAPI(url=settings.SALT_API['url'],username=settings.SALT_API['user'],password=settings.SALT_API['password'])

def test_sapi():

    print sapi.remote_localexec('unicomrecharge_server6.ctu.com','cmd.run','cd c:\\salt\\bin & python c:\\UnicomRechargeV2/logger.py -c cat_log -eid E_1 -st "2017-08-25 09:50" -et "2017-08-25 10:46" -l 50','list')


def test_stop_program():
    print sapi.remote_execution('unicomrecharge_server6.ctu.com','cmd.run','cd c:\\salt\\bin & python c:\\UnicomRechargeV2/manage.py start wap E_1','list')


test_stop_program()