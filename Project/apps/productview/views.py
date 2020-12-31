from django.shortcuts import render
from django.views.generic import View
from utils.mixin import LoginRequiredMixin
from productview.models import ProductTable, ProductPictureTable, ProductVersionTable, ProductPerformTable, NewProductTable, ProductPriceTable, ProductRecordTable, RotationProductTable, HardwareProductTable, SoftwareProductTable
# Create your views here.


# http://127.0.0.1:8000 产品首页
class IndexView(View):
    """首页"""
    def get(self, request):

        product = ProductTable.objects.all()
        product_picture = ProductPictureTable.objects.all()
        product_version = ProductVersionTable.objects.all()
        rotation_picture = RotationProductTable.objects.all()

        context = {
            'product': product,
            'product_picture': product_picture,
            'product_version': product_version,
            'rotation_picture': rotation_picture,
        }

        return render(request, 'index.html', context)


# 产品中心页
class ProductView(LoginRequiredMixin, View):
    """产品中心页"""
    def get(self, request):

        hardware = HardwareProductTable.objects.all()
        software = SoftwareProductTable.objects.all()
        price = ProductPriceTable.objects.all()

        context = {
            'hardware': hardware,
            'software': software,
            'price': price,
        }
        return render(request, 'product_intro.html', context)


# 产品参数配置页
class ProductParam(LoginRequiredMixin, View):
    """"产品参数配页"""
    def get(self, request):

        product_rec = ProductRecordTable.objects.all()
        product_per = ProductPerformTable.objects.all()

        context = {
            'product_rec': product_rec,
            'product_per': product_per
        }
        return render(request, 'product_param.html', context)
