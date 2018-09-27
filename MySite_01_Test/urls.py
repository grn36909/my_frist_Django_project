"""MySite_01_Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
# from django.views.generic.base import RedirectView
# from django.contrib.staticfiles.views import serve
# from django.http import Http404
# from polls import views as pools_views  # 导入pools应用中的views.py文件, 为防止文件名冲突使用as重命名


urlpatterns = [

    # exp: /polls/...
    re_path(r'^polls/', include('polls.urls')),

    # exp: /grn31.admin/...
    re_path(r'^grn31/admin/', admin.site.urls),   # 后台管理url (admin/admin)

    # exp: /favicon.ico
    # re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/admin/img/favicon.ico')),    # 此方法会产生重定向,不推荐
    # path('favicon.ico', serve, {'path': 'static/admin/img/favicon.ico'}),                     # 无效

    # exp: /...
    # re_path(r'.*', include('polls.urls')),
]
