#coding: utf-8


'''程序管理类
'''
from devops import settings
from deploy.models import  SaltHost
from  deploy.saltapi import SaltAPI

def get_os_type(saltapi,nodename):
    if nodename == '0':
        return None
    ret = saltapi.remote_localexec(nodename,"grains.item","os","list")
    return ret[nodename]['os']


def get_project_dir(os_type):
    if os_type == "Windows":
        return settings.PROJECT_UNICOMRECHARGE['projectdir_windows']
    elif os_type == "CentOS":
        return  settings.PROJECT_UNICOMRECHARGE['projectdir_linux']
    return None

def get_salt_dir(os_type):
    if os_type == "Windows":
        return settings.PROJECT_UNICOMRECHARGE['saltdir_windows']
    elif os_type == "CentOS":
        return settings.PROJECT_UNICOMRECHARGE['saltdir_linux']


def format_remotecmd(saltdir,projectdir,cmd_tag,program_id):
    version = "wap"
    return "cd %s & python %s/manage.py -c %s -eid %s -v %s"%(saltdir,projectdir,cmd_tag,program_id,version)

def run_cmd(nodename,program_id,tag):
    sapi = SaltAPI(url=settings.SALT_API['url'],username=settings.SALT_API['user'],password=settings.SALT_API['password'])
    os_type  = get_os_type(sapi,nodename)
    get_project_dir(os_type)
    saltdir = get_salt_dir(os_type)
    projectdir = get_project_dir(os_type)
    arg = format_remotecmd(saltdir,projectdir,tag,program_id)
    tgt,fun,arg,expr_form = nodename,"cmd.run",arg,"list"
    print (tgt,fun,arg,expr_form)
    #sapi.remote_execution(tgt,fun,arg,expr_form)