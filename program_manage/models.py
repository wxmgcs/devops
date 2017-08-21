#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Program(models.Model):
    program_id = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'程序编号')
    status = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'状态')
    type = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'程序类型')
    vpn_code = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'VPN编号')
    ip_addr = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'IP地址')
    os_type = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'系统类型')
    nodename = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'节点名')

    def __unicode__(self):
        return self.program_id

    class Meta:
        default_permissions = ()
