from django.contrib import admin
from .models import UserEntity



class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'phone')
    list_per_page = 3
# Register your models here.
admin.site.register(UserEntity, UserAdmin)