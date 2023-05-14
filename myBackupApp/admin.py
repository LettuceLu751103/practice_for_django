from django.contrib import admin
from .models import UserEntity, CategoryEntity, DeviceEntity



class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'phone')
    list_per_page = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'vendor', 'category')

# Register your models here.
admin.site.register(UserEntity, UserAdmin)
admin.site.register(CategoryEntity, CategoryAdmin)
admin.site.register(DeviceEntity, DeviceAdmin)