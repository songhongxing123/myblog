#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/21 1:30 PM
# @Author : songhx
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    gender = models.IntegerField(null=True)


class User(models.Model):
    name = models.CharField(max_length=50)
    nickName = models.CharField(max_length=200, null=True)

class Order(models.Model):
    uuid = models.CharField(max_length=32, primary_key=True)
    orderNo = models.CharField(max_length=50, db_column='order_no')
    ownerName = models.CharField(max_length=255,db_column='owner_name',null=True)


    def __str__(self):
        return self.uuid

    def getOwner(self):
        return self.ownerName

    class Meta:
        db_table = "order"