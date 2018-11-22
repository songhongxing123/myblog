from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField(max_length=2, null=True)
    gender = models.IntegerField(max_length=1, null=True)


class User(models.Model):
    name = models.CharField(max_length=50)
    nickName = models.CharField(max_length=200, null=True)

class Order(models.Model):
    uuid = models.CharField(max_length=32, primary_key=True)
    orderNo = models.CharField(max_length=50, name='订单', db_column='order_no')

    class Meta:
        db_table = "order"