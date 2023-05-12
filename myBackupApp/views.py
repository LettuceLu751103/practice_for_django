from django.http import HttpRequest
from django.shortcuts import render, redirect
from myBackupApp.models import UserEntity
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