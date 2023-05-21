from django.contrib import admin
from .models import OrderModel

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'price', 'pay_type', 'current_status', 'receiver', 'receiver_address', 'receiver_phone')


admin.site.register(OrderModel, OrderAdmin)