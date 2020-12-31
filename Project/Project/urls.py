"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),   # 后台管理模块
    path('tinymce/', include('tinymce.urls')),  # 富文本编辑器
    path('user/', include(('user.urls', 'user'), namespace='user')),   # 用户模块
    path('intellprop/', include(('intellprop.urls', 'intellprop'), namespace='intellprop')),   # 知识产权模块
    path('', include(('productview.urls', 'productview'), namespace='productview')),   # 产品模块


]
