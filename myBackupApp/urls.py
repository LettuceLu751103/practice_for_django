from django.urls import path
from myBackupApp.views import user_list

from myBackupApp.views import add_user, find_device, find_device_json

urlpatterns = [
    path('list', user_list),
    path('add_user', add_user),
    path('find_device', find_device),
    path('find_device_json', find_device_json)
]
