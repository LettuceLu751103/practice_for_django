from django.db import models

# Create your models here.

class UserEntity(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        # 配置表名
        db_table = 't_user'
        verbose_name = '用戶管理'
        verbose_name_plural = verbose_name

class CategoryEntity(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        verbose_name = '類別管理'
        verbose_name_plural = verbose_name

class DeviceEntity(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(verbose_name='價格')
    vendor = models.CharField(max_length=30)
    category = models.ForeignKey('CategoryEntity', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    '''
    Warning: By default on_delete=models.CASCADE, which means that if the author was deleted, 
    this book would be deleted too! We use SET_NULL here, 
    but we could also use PROTECT or RESTRICT to prevent the author being deleted while any book uses it.
    '''

    class Meta:
        db_table = 't_device'
        verbose_name = '設備管理'
        verbose_name_plural = verbose_name