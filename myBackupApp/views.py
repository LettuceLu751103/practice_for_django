from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import UserEntity

from .models import DeviceEntity


# Create your views here.

def user_list(request):
    # users = [
    #     {'id':1, 'name': 'Lettuce'},
    #     {'id':2, 'name': 'Joy'},
    #     {'id':3, 'name': 'Jack'},
    #     {'id':4, 'name': 'Mark'},
    # ]
    users = UserEntity.objects.all()
    print(users)
    return render(request, 'user/list.html', locals())

def add_user(request):

    u1 = UserEntity()
    u1.name = 'Joy Chan'
    u1.age = 35
    u1.phone = '0986395127'
    u1.save()

    return redirect('/user/list')


def find_device(request):

    # 從查詢參數中獲取價格區間 price1, price2 之間有哪些設備使用 filter
    # 以下的範例查詢 price >= 20000, price <= 47000
    price1 = 1000
    price2 = 47000
    results = DeviceEntity.objects.filter(price__gte=price1).filter(price__lte=price2).all()
    print(results)
    return render(request, 'device/list.html', locals())
