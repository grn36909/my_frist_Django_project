#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'GRN31'

from django.urls import re_path
from . import views

app_name = 'polls'

urlpatterns = [
    # exp: /polls/
    re_path(r'^$', views.IndexView.as_view(), name='index'),

    # exp: /polls/hello/
    re_path(r'^hello/', views.hello, name='hello'),

    # exp: /polls/1/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # exp: /polls/1/results/
    re_path(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # exp: /polls/1/vote/
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # exp: 404
    re_path(r'.*', views.err_404, name='ERROR'),
]
