from django.urls import path
from intellprop import views
from django.conf.urls import url
from intellprop.views import IntellpropRecord


urlpatterns = [
    path('intellprop_index', views.intellprop_index, name='intellprop_index'),  # 知识产权首页
    url(r'^intellprop_record$', IntellpropRecord.as_view(), name='intellprop_record'),  # 知识产权记录

]


