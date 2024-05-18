from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# 유저 커스텀한 유저 admin에서 관리하기 위한 작업1 (필요하면 넣으면 됨)
admin.site.register(User, UserAdmin)
