from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser, models.Model):
    """用户模型类"""

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
