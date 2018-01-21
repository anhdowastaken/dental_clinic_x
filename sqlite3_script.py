import os, sys
sys.path.append('/home/anhdo/Desktop/dental_clinic_x')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()

from django.contrib.auth.models import User
from dental_clinic_x.models import DentalClinicUser
from dental_clinic_x.models import DentalService

try:
    # Admin Trang Tran
    user = User.objects.create_user(username = 'AD1', password = 'dcx12345')
    user.first_name = 'Trang'
    user.last_name = 'Tran'
    user.is_staff = False
    user.is_superuser = False
    user.save()
    user.dentalclinicuser.role = 'a'
    user.dentalclinicuser.save()
except:
    pass

try:
    # Admin Yen Le
    user = User.objects.create_user(username = 'AD2', password = 'dcx12345')
    user.first_name = 'Yen'
    user.last_name = 'Le'
    user.is_staff = False
    user.is_superuser = False
    user.save()
    user.dentalclinicuser.role = 'a'
    user.dentalclinicuser.save()
except:
    pass

try:
    # Dentist Long Nguyen
    user = User.objects.create_user(username = 'NS1', password = 'dcx12345')
    user.first_name = 'Long'
    user.last_name = 'Nguyen'
    user.is_staff = False
    user.is_superuser = False
    user.save()
    user.dentalclinicuser.role = 'd'
    user.dentalclinicuser.save()
except:
    pass

try:
    # Dentist Phuc Nguyen
    user = User.objects.create_user(username = 'NS2', password = 'dcx12345')
    user.first_name = 'Phuc'
    user.last_name = 'Nguyen'
    user.is_staff = False
    user.is_superuser = False
    user.save()
    user.dentalclinicuser.role = 'd'
    user.dentalclinicuser.save()
except:
    pass

try:
    # Dental service
    dental_service = DentalService()
    dental_service.name = 'Computer Tomography (3D scan)'
    dental_service.currency = 'usd'
    dental_service.price = 100
    dental_service.save()
except:
    pass

try:
    # Dental service
    dental_service = DentalService()
    dental_service.name = 'Digital panoramic X-ray'
    dental_service.currency = 'usd'
    dental_service.price = 20
    dental_service.save()
except:
    pass

try:
    # Dental service
    dental_service = DentalService()
    dental_service.name = 'Digital dental X-ray'
    dental_service.currency = 'usd'
    dental_service.price = 10
    dental_service.save()
except:
    pass
