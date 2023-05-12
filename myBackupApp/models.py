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
