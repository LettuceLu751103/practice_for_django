from django.db.models import Max, Min, Avg, Sum
from django.http import HttpRequest, JsonResponse
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
    origins = DeviceEntity.objects.all().order_by('price')
    originsCount = DeviceEntity.objects.all().count()
    singlefirstObj = DeviceEntity.objects.first()
    singleLastObj = DeviceEntity.objects.last()
    price1 = request.GET.get('price1', 0)
    price2 = request.GET.get('price2', 500000)
    price3 = request.GET.get('price3', 0)
    results = DeviceEntity.objects.filter(price__gte=price1).filter(price__lte=price2).exclude(price=price3).all()
    resultsCount = DeviceEntity.objects.filter(price__gte=price1).filter(price__lte=price2).exclude(price=price3).all().count()
    print(singlefirstObj)
    return render(request, 'device/list.html', locals())

def find_device_json(request):
    results = {}
    results_list = []
    datas = DeviceEntity.objects.values()
    for data in datas:
        print(data)
        results_list.append(data)
    results['count'] = DeviceEntity.objects.count()
    results['msg'] = '查詢到數據'
    results['data'] = results_list
    results['agg'] = DeviceEntity.objects.aggregate(Max('price'), Min('price'), Avg('price'), Sum('price'))


    return JsonResponse(results)