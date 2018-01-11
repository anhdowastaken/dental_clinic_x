from django.contrib import admin
from .models import DentalClinicUser
from .models import MedicalHistory
from .models import DentalHistory
from .models import DentalService
from .models import DentalRecord
from .models import Examination

admin.site.register(DentalClinicUser)
admin.site.register(MedicalHistory)
admin.site.register(DentalHistory)
admin.site.register(DentalService)
admin.site.register(DentalRecord)
admin.site.register(Examination)
