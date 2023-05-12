from django.urls import path
from myBackupApp.views import user_list

from myBackupApp.views import add_user

urlpatterns = [
    path('list', user_list),
    path('add_user', add_user)
]
