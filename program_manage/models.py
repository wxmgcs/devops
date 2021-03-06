#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Program(models.Model):
    program_id = models.CharField(max_length=255, default='', blank=True, null=True, unique=True,verbose_name=u'程序编号',
                                  error_messages={'required': u'程序名不能为空'})
    status = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'状态')
    type = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'程序类型')
    vpn_code = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'VPN编号')
    area_ip = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'局域网IP')
    remote_ip = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'外网IP')
    os_type = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'系统类型')
    nodename = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'节点名')

    def __unicode__(self):
        return self.program_id

    class Meta:
        default_permissions = ()
