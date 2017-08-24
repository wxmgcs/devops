#coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class VPN(models.Model):

    user_name = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'VPN账号')
    pwd = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'VPN密码')
    status = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'状态')
    area_ip = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'局域网ip')
    remote_ip = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'外网ip')

    def __unicode__(self):
        return self.user_name

    class Meta:
        default_permissions = ()