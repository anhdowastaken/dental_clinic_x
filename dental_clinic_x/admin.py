from django.contrib import admin
from .models import DentalClinicUser
from .models import DentalService
from .models import DentalRecord
from .models import Examination
from .models import DentalServiceQuantity

class DentalServiceQuantityInline(admin.TabularInline):
    model = DentalServiceQuantity

class ExaminationAdmin(admin.ModelAdmin):
    inlines = (DentalServiceQuantityInline, )

admin.site.register(DentalClinicUser)
admin.site.register(DentalService)
admin.site.register(DentalRecord)
admin.site.register(Examination, ExaminationAdmin)

