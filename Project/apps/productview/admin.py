from django.contrib import admin
from productview.models import ProductTable, ProductPictureTable, ProductVersionTable, ProductPerformTable, NewProductTable, ProductPriceTable, ProductRecordTable, RotationProductTable
# Register your models here.


admin.site.register(ProductTable)
admin.site.register(ProductPictureTable)
admin.site.register(ProductVersionTable)
admin.site.register(ProductPerformTable)
admin.site.register(NewProductTable)
admin.site.register(ProductPriceTable)
admin.site.register(ProductRecordTable)
admin.site.register(RotationProductTable)
