from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from . import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'upload_genorder/$', views.upload_genorder_result),


]
