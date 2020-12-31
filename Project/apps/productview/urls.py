from django.conf.urls import url
from productview.views import IndexView, ProductView,ProductParam


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),  # 首页
    url(r'^product_intro$', ProductView.as_view(), name='product_intro'),  # 产品介绍
    url(r'^product_param$', ProductParam.as_view(), name='product_param'),   # 产品参数

]
