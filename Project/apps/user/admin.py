from django.contrib import admin
from user.models import User
# Register your models here.


admin.site.site_header = '产品教学平台后台登录'
admin.site.site_title = '产品教学平台的后台管理'
admin.site.register(User)