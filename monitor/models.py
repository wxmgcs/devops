#coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UnicomRechargeGenOrder(models.Model):
    eid = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name=u'程序编号',
                                  error_messages={'required': u'程序名不能为空'})
    status = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'下单状态')
    vpn_code = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'vpn编号')
    create_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.eid

    class Meta:
        default_permissions = ()
