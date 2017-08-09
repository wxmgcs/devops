# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-12 01:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userauth', '0001_initial'),
        ('deploy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salthost',
            name='department',
            field=models.ManyToManyField(related_name='host_department_set', to='userauth.Department', verbose_name='\u6240\u5c5e\u90e8\u95e8'),
        ),
        migrations.AddField(
            model_name='salthost',
            name='user_group',
            field=models.ManyToManyField(related_name='host_usergroup_set', to='userauth.UserGroup', verbose_name='\u6240\u5c5e\u7528\u6237\u7ec4'),
        ),
        migrations.AddField(
            model_name='saltgroup',
            name='department',
            field=models.ManyToManyField(blank=True, related_name='saltgroup_department_set', to='userauth.Department', verbose_name='\u6240\u5c5e\u90e8\u95e8'),
        ),
        migrations.AddField(
            model_name='saltgroup',
            name='minions',
            field=models.ManyToManyField(related_name='salt_host_set', to='deploy.SaltHost', verbose_name='Salt\u4e3b\u673a'),
        ),
        migrations.AddField(
            model_name='saltgroup',
            name='user_group',
            field=models.ManyToManyField(related_name='group_usergroup_set', to='userauth.UserGroup', verbose_name='\u6240\u5c5e\u7528\u6237\u7ec4'),
        ),
        migrations.AddField(
            model_name='projectrollback',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deploy.Project'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='user_group',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_usergroup_set', to='userauth.UserGroup', verbose_name='\u7528\u6237\u7ec4'),
        ),
        migrations.AddField(
            model_name='moduleupload',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moduleupload',
            name='user_group',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module_usergroup_set', to='userauth.UserGroup', verbose_name='\u6240\u5c5e\u7528\u6237\u7ec4'),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='filerollback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
