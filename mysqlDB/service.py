#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/22 6:01 PM
# @Author : songhx
# @File   : service.py

from .models import Order
import uuid
import time
import random

#查找所有列表
def findOrder():
    sql = "select a.uuid,a.order_no,a.owner_name ownerName,b.nickName from `order` a left join user b on a.order_no = b.name"
    #执行自定义SQL
    orders = Order.objects.raw(sql)
    #执行单表查询
    #orders = Order.objects.all()
    for order in orders:
        print(order.getOwner())
    return orders

#新增记录
def save():
    suuid = str(uuid.uuid1()).replace('-', '')
    orderNo = "GD" + time.strftime('%Y%m%d',time.localtime(time.time())) + str(random.randrange(1000,9999))
    Order.objects.create(uuid=suuid, orderNo=orderNo, ownerName='阿瑟大')


