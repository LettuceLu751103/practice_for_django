from django.db import models

# Create your models here.

class UserEntity(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=10)


    class Meta:
        # 配置表名
        db_table = 't_user'

