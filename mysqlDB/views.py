from django.shortcuts import render
from . import models, service
from django.db import connection
from django.db.transaction import commit
from django.http import HttpResponse




def findOrder(request):
    orders = service.findOrder()
    return render(request, 'order/index.html', {'orders': orders})

def saveOrder(request):
    service.save()
    orders = service.findOrder()
    return render(request, 'order/index.html', {'orders': orders})