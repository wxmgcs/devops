#coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Log(models.Model):
    title = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'标题')
    content = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'内容')
    peer = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'邮件')
    create_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        default_permissions = ()


class Peer(models.Model):
    peer = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'邮件')
    status = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.peer

    class Meta:
        default_permissions = ()