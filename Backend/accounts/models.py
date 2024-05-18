from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 유저 커스텀한 유저를 사용하기 위한 작업1
class User(AbstractUser):
    # nickname = models.CharField(max_length=100)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followings')