from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 유저 커스텀한 유저를 사용하기 위한 작업1
class User(AbstractUser):
    # nickname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='images/sample.png')
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical = False ,related_name='followings')