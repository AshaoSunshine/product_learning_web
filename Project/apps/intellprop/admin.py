from django.contrib import admin
from intellprop.models import IntellPropRecordTable, SoftworkTable, ViewSoftworkTable, NewSoftworkTable,DeleteSoftworkTable,PaperTable,ViewPaperTable,NewPaperTable,DeletePaperTable,PatentTable,ViewPatentTable,NewPatentTable,DeletePatentTable

# Register your models here.


admin.site.register(IntellPropRecordTable)
admin.site.register(SoftworkTable)
admin.site.register(ViewSoftworkTable)
admin.site.register(NewSoftworkTable)
admin.site.register(DeleteSoftworkTable)
admin.site.register(PaperTable)
admin.site.register(ViewPaperTable)
admin.site.register(NewPaperTable)
admin.site.register(DeletePaperTable)
admin.site.register(PatentTable)
admin.site.register(ViewPatentTable)
admin.site.register(NewPatentTable)
admin.site.register(DeletePatentTable)

