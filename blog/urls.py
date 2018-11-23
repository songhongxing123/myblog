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
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action/$', views.edit_action, name='edit_action'),
]