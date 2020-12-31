from django.conf.urls import url
from user.views import LoginView, LogoutView,RegisterView


urlpatterns = [

    url(r'^login$', LoginView.as_view(), name='login'),  # 登录
    url(r'^logout$', LogoutView.as_view(), name='logout'),  # 注销登录
    url(r'^register$', RegisterView.as_view(), name='register'),  # 注册

]