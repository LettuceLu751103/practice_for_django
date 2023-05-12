"""
URL configuration for myFirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path, include

def index(request:HttpRequest):
    print(request.GET)
    users = [
        {'id':1, 'name':'Lettuce'},
        {'id':2, 'name':'Joy'}
    ]
    print(locals())
    return render(request, 'index.html', locals())
    # return HttpResponse('<h1 style="color:green">hi, Django</h1>'.encode('utf-8'))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index),
    path('user/', include('myBackupApp.urls'))
]
