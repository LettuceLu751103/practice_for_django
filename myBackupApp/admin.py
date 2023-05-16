from django.contrib import admin
from .models import UserEntity, CategoryEntity, DeviceEntity, Company



class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'phone')
    list_per_page = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'vendor', 'category')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'phone', 'address', 'logo', 'opend', 'created_at', 'updated_at')


# Register your models here.
admin.site.register(UserEntity, UserAdmin)
admin.site.register(CategoryEntity, CategoryAdmin)
admin.site.register(DeviceEntity, DeviceAdmin)
admin.site.register(Company, CompanyAdmin)