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


class Company(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company', null=True, blank=True, width_field='logo_width', height_field='logo_height')
    logo_width = models.IntegerField(null=True, blank=True)
    logo_height = models.IntegerField(null=True, blank=True)
    opend = models.BooleanField(default=False)
    remark = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tt_company'
        verbose_name = '公司管理'
        verbose_name_plural = verbose_name