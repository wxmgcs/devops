"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url

from deploy import views as dviews
from userperm import views as uviews
from asset import views as aviews
from monitor import views as monitor_views
from program_manage import views as program_views
from logger_manage import views as logger_views
from vpn_manage import views as vpn_views
from monitor import views as monitor_views
from alarm import views as alarm_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('userauth.urls')),
    url(r'^user_perm/exec/$', uviews.user_command_list, name='command_list'),
    url(r'^user_perm/exec/manage/add/$', uviews.user_command_manage, name='command_add'),
    url(r'^user_perm/exec/manage/delete/$', uviews.user_command_manage, name='command_delete'),
    url(r'^user_perm/exec/manage/(?P<id>\d+)/edit/$', uviews.user_command_manage, name='command_edit'),
    url(r'^user_perm/dir/$', uviews.user_dir_list, name='dir_list'),
    url(r'^user_perm/dir/manage/add/$', uviews.user_dir_manage, name='dir_add'),
    url(r'^user_perm/dir/manage/delete/$', uviews.user_dir_manage, name='dir_delete'),
    url(r'^user_perm/dir/manage/(?P<id>\d+)/edit/$', uviews.user_dir_manage, name='dir_edit'),
    url(r'^deploy/key_list/$', dviews.salt_key_list, name='key_list'),
    url(r'^deploy/program_list/$', dviews.salt_program_list, name='program_list'),
    url(r'^deploy/key_list_import/$', dviews.salt_key_import, name='key_import'),
    url(r'^deploy/key_manage$', dviews.salt_key_manage, name='key_add'),
    url(r'^deploy/key_manage$', dviews.salt_key_manage, name='key_delete'),
    url(r'^deploy/key_manage$', dviews.salt_key_manage, name='key_flush'),
    url(r'^deploy/key_manage$', dviews.salt_key_manage, name='key_manage'),
    url(r'^deploy/group_list/$', dviews.salt_group_list, name='group_list'),
    url(r'^deploy/group_manage/add/$', dviews.salt_group_manage, name='group_add'),
    url(r'^deploy/group_manage/delete$', dviews.salt_group_manage, name='group_delete'),
    url(r'^deploy/group_manage/(?P<id>\d+)/edit/$', dviews.salt_group_manage, name='group_edit'),
    url(r'^deploy/module_list/$', dviews.salt_module_list, name='module_list'),
    url(r'^deploy/module_manage/add/$', dviews.salt_module_manage, name='module_add'),
    url(r'^deploy/module_manage/delete$', dviews.salt_module_manage, name='module_delete'),
    url(r'^deploy/module_manage/(?P<id>\d+)/edit/$', dviews.salt_module_manage, name='module_edit'),
    url(r'^deploy/remote_execution/$', dviews.salt_remote_exec, name='remote_exec'),
    url(r'^deploy/remote_execution/exec/$', dviews.salt_ajax_remote_exec, name='ajax_exec'),
    url(r'^deploy/advanced_manage/$', dviews.salt_advanced_manage, name='advanced_manage'),
    url(r'^deploy/remote_exec/check_result/$', dviews.salt_ajax_result, name='ajax_result'),
    url(r'^deploy/module_deploy/$', dviews.salt_module_deploy, name='module_deploy'),
    url(r'^deploy/module_deploy/deploy/$', dviews.salt_ajax_module_deploy, name='ajax_deploy'),
    url(r'^deploy/file_manage/download/$', dviews.salt_file_download, name='file_download'),
    url(r'^deploy/file_manage/upload/$', dviews.salt_file_upload, name='file_manage'),
    url(r'^deploy/file_manage/upload/ajax_upload$', dviews.salt_ajax_file_upload, name='file_ajax'),
    url(r'^deploy/file_manage/rollback/$', dviews.salt_file_rollback, name='file_rollback'),
    url(r'^deploy/file_manage/rollback/ajax_rollback$', dviews.salt_ajax_file_rollback, name='ajax_rollback'),
    url(r'^deploy/task_list/$', dviews.salt_task_list, name='task_list'),
    url(r'^deploy/task_check/$', dviews.salt_task_check, name='task_check'),
    url(r'^deploy/task_running/$', dviews.salt_task_running, name='task_running'),
    url(r'^deploy/group_minions/$', dviews.salt_ajax_minions, name='ajax_minions'),
    url(r'^deploy/project_list/$', dviews.project_list, name='project_list'),
    url(r'^deploy/project_manage/add/$', dviews.project_manage, name='project_add'),
    url(r'^deploy/project_manage/delete$', dviews.project_manage, name='project_delete'),
    url(r'^deploy/project_manage/(?P<id>\d+)/edit/$', dviews.project_manage, name='project_edit'),
    url(r'^deploy/project_manage/deploy/$', dviews.project_deploy, name='project_deploy'),
    url(r'^audit/log_audit/$', uviews.audit_log, name='log_audit'),
    
    url(r'^asset/server_info/$', aviews.get_server_asset_info, name='server_info'),
    url(r'^asset/idc/list/$', aviews.idc_asset_list, name='idc_asset_list'),
    url(r'^asset/idc/add/$', aviews.idc_asset_manage, name='idc_add'),
    url(r'^asset/idc/edit/(?P<aid>\d+)/(?P<action>[\w-]+)/$', aviews.idc_asset_manage, name='idc_manage'),
    url(r'^asset/load_city/$', aviews.geo_input, name='load_city'),
    
    url(r'^monitor/control_board/$',monitor_views.control_board,name='control_board'),
    
    url(r'^program_manage/list/$',program_views.program_list,name='program_list'),
    url(r'^program_manage/add/$',program_views.add,name='program_add'),
    url(r'^program_manage/edit/(?P<id>\d+)/$',program_views.program_edit,name='program_edit'),
    url(r'^program_manage/delete/(?P<id>\d+)/$',program_views.program_delete,name='program_delete'),
    url(r'^program_manage/stop/(?P<id>\d+)/$',program_views.program_stop,name='program_stop'),
    url(r'^program_manage/start/(?P<id>\d+)/$',program_views.program_start,name='program_start'),
    url(r'^program_manage/restart/(?P<id>\d+)/$',program_views.program_restart,name='program_restart'),

    url(r'^logger_manage/logger_list/$',logger_views.list,name='logger_list'),
    url(r'^logger_manage/show_logger/(?P<id>\d+)/$',logger_views.show_logger,name='show_logger'),
    url(r'^logger_manage/get_programid/$',logger_views.get_programid,name='get_programid'),
    url(r'^logger_manage/get_allprogramid/$',logger_views.get_allprogramid,name='get_allprogramid'),
    
    url(r'^vpn_manage/edit/(?P<id>\d+)/$',vpn_views.edit,name='vpn_edit'),
    url(r'^vpn_manage/list/$',vpn_views.list,name='vpn_list'),
    url(r'^vpn_manage/add/$',vpn_views.edit,name='vpn_add'),
    url(r'^vpn_manage/delete/(?P<id>\d+)/$',vpn_views.delete,name='vpn_delete'),
    url(r'^vpn_manage/get_config/$',vpn_views.get_config,name='get_vpnconfig'),

    
    url(r'^deploy/page_test$',dviews.page_test,name='page_test'),

    url(r'^monitor/unicomrecharge/upload_genorder',monitor_views.upload_genorder,name='upload_genorder'),
    url(r'^monitor/alarm/',alarm_views.send_alarm,name='send_alarm'),
    url(r'^monitor/statics_vpn_status/',monitor_views.statics_vpn_status,name='statics_vpn_status'),
    url(r'^monitor/get_fixed_vpn/',monitor_views.get_fixed_vpn,name='get_fixed_vpn'),


]
