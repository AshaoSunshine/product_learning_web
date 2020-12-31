from django.shortcuts import render
from django.views.generic import View
from django.core.cache import cache
# Create your views here.


# 首页
def intellprop_index(request):
    return render(request, 'intellprop_index.html')


# 知识产权记录页
class IntellpropRecord(View):
    """"知识产权记录页"""
    def get(self, request):
        # 尝试从缓存中获取数据
        context = cache.get('index_page_data')

        # 使用模板
        return render(request, 'intellprop_record.html', context)


