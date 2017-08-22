# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-21 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='VPN\u7f16\u53f7')),
                ('pwd', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='IP\u5730\u5740')),
                ('status', models.IntegerField(blank=True, default=0, null=True, verbose_name='\u72b6\u6001')),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]