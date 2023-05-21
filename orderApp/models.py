from django.db import models


# 創建抽象類, 當作每一個類別的時間屬性
class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='創建時間')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新時間')

    class Meta:
        abstract = True


# Create your models here.
class OrderModel(BaseModel):
    num = models.CharField(max_length=30, primary_key=True, verbose_name='訂單編號')
    title = models.CharField(max_length=100, verbose_name='訂單名稱')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='訂單價格')
    pay_type = models.IntegerField(choices=((0, '餘額支付'), (1, '銀行卡支付'), (2, '微信支付'), (3, '支付寶支付'), (4, 'Line Pay 支付')),
                                   verbose_name='支付方式',
                                   default=0)
    current_status = models.IntegerField(choices=((0, '待支付'), (1, '已支付'), (2, '待收貨'), (3, '已收貨'), (4, '完成'), (5, '取消')),
                                         verbose_name='當前狀態',
                                         default=0)
    receiver = models.CharField(max_length=30, verbose_name='收貨人')
    receiver_address = models.CharField(max_length=100, verbose_name='收貨地址')
    receiver_phone = models.CharField(max_length=10, verbose_name='收貨人電話')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_order'
        verbose_name = '訂單表'
        verbose_name_plural = verbose_name

