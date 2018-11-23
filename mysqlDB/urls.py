#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/21 1:30 PM
# @Author : songhx
# @File   : urls.py

from django.conf.urls import url

from . import views

app_name = 'order'
urlpatterns = [
    #正则表达式^开始$结束，
    url(r'^list/$', views.findOrder),
    url(r'^save/$', views.saveOrder),
]