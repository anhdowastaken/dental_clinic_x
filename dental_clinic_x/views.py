from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist

from .models import DentalClinicUser
from .models import DentalRecord
from .models import DentalService

from .forms import DentalRecordForm
from .forms import DentistProfileForm
from .forms import DentalServiceForm

def admin_check(user):
    if user.is_authenticated:
        return user.dentalclinicuser.is_admin()
    else:
        return False

def dentist_check(user):
    if user.is_authenticated:
        return user.dentalclinicuser.is_dentist()
    else:
        return False

def patient_check(user):
    if user.is_authenticated:
        return user.dentalclinicuser.is_patient()
    else:
        return False

@login_required
def index(request):
    user = request.user
    if user.dentalclinicuser.is_admin():
        # Get all dental records of the dental clinic
        dental_records = DentalRecord.objects.all()
        context = {
            'dental_records': dental_records,
        }
        template = loader.get_template('index_admin.html')
        return HttpResponse(template.render(context, request))

    elif user.dentalclinicuser.is_dentist():
        # Get all dental records which current dentist is in charge of
        dental_records = DentalRecord.objects.filter(dentists__id__exact = user.dentalclinicuser.id)
        context = {
            'dental_records': dental_records,
        }
        template = loader.get_template('index_dentist.html')
        return HttpResponse(template.render(context, request))

    elif user.dentalclinicuser.is_patient():
        # Get all dental records of current patient
        dental_records = DentalRecord.objects.filter(patient__id__exact = user.dentalclinicuser.id)
        context = {
            'dental_records': dental_records,
        }
        template = loader.get_template('index_patient.html')
        return HttpResponse(template.render(context, request))

    else:
        template = loader.get_template('index.html')
        context = {}
        return HttpResponse(template.render(context, request))

@login_required
def view_dental_record_list(request):
    return redirect('dental_clinic_x:index')

@login_required
@user_passes_test(admin_check, 'dental_clinic_x:index')
def new_dental_record(request):
    template = loader.get_template('new_dental_record.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(admin_check, 'dental_clinic_x:index')
def create_new_dental_record(request):
    if request.method == 'POST':
        dental_record_form = DentalRecordForm(request.POST)
        if dental_record_form.is_valid():
            try:
                # Find dummy user
                user = User.objects.get(username = "dummy_username")
                # If a dummy user exists, it should not be there
                user.delete()
            except ObjectDoesNotExist:
                pass

            # Create a dummy user with default password
            user = User.objects.create_user(username = "dummy_username", password = "dcx12345")
            user.is_staff = False
            user.is_superuser = False
            user.save()
            # Set new username by using its new ID
            user.username = "BN" + str(user.id)
            user.first_name = dental_record_form.cleaned_data['first_name']
            user.last_name = dental_record_form.cleaned_data['last_name']
            user.save()

            # User created by admin should be a patient
            user.dentalclinicuser.role = 'p'
            user.dentalclinicuser.save()

            # Create new dental record for new patient above
            dental_record = DentalRecord(patient = user.dentalclinicuser)
            dental_record.medical_history_operations = dental_record_form.cleaned_data['medical_history_operations']
            dental_record.medical_history_nursing = dental_record_form.cleaned_data['medical_history_nursing']
            dental_record.medical_history_pregnant = dental_record_form.cleaned_data['medical_history_pregnant']
            dental_record.dental_history_bad_breath = dental_record_form.cleaned_data['dental_history_bad_breath']
            dental_record.dental_history_sensitive_teeth = dental_record_form.cleaned_data['dental_history_sensitive_teeth']
            dental_record.save()

        return redirect('dental_clinic_x:index')
    else:
        return redirect('dental_clinic_x:index')

@login_required
def view_dental_record(request, record_id):
    if record_id is None:
        return redirect('dental_clinic_x:index')
    else:
        user = request.user

        if user.dentalclinicuser.is_admin():
            print("admin")
            dental_record = DentalRecord.objects.get(id__exact = record_id)

            context = {
                'has_permission': True,
                'dental_record': dental_record,
            }
            template = loader.get_template('view_dental_record.html')
            return HttpResponse(template.render(context, request))

        elif user.dentalclinicuser.is_dentist():
            print("dentist")
            dental_record = DentalRecord.objects.get(id__exact = record_id)

            if user.dentalclinicuser in dental_record.dentists.all():
                has_permission = True
            else:
                has_permission = False

            context = {
                'has_permission': has_permission,
                'dental_record': dental_record,
            }
            template = loader.get_template('view_dental_record.html')
            return HttpResponse(template.render(context, request))

        elif user.dentalclinicuser.is_patient():
            print("patient")
            dental_record = DentalRecord.objects.get(id__exact = record_id)

            if user.dentalclinicuser == dental_record.patient:
                has_permission = True
            else:
                has_permission = False

            context = {
                'has_permission': has_permission,
                'dental_record': dental_record,
            }
            template = loader.get_template('view_dental_record.html')
            return HttpResponse(template.render(context, request))

        else:
            return redirect('dental_clinic_x:index')

@login_required
def view_dentist_list(request):
    user = request.user
    # Get all dentists of the dental clinic
    dentists = DentalClinicUser.objects.filter(role__exact = 'd')
    context = {
        'dentists': dentists,
    }
    template = loader.get_template('view_dentist_list.html')
    return HttpResponse(template.render(context, request))

@login_required
def view_dentist(request, dentist_id):
    pass

@login_required
def view_dental_service_list(request):
    user = request.user
    # Get all dental services of the dental clinic
    dental_services = DentalService.objects.all()
    context = {
        'dental_services': dental_services,
    }
    template = loader.get_template('view_dental_service_list.html')
    return HttpResponse(template.render(context, request))

@login_required
def view_dental_service(request, service_id):
    pass

@login_required
@user_passes_test(admin_check, 'dental_clinic_x:index')
def new_dentist_profile(request):
    template = loader.get_template('new_dentist_profile.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(admin_check, 'dental_clinic_x:index')
def create_new_dentist_profile(request):
    if request.method == 'POST':
        dentist_profile_form = DentistProfileForm(request.POST)
        if dentist_profile_form.is_valid():
            try:
                # Find dummy user
                user = User.objects.get(username = "dummy_username")
                # If a dummy user exists, it should not be there
                user.delete()
            except ObjectDoesNotExist:
                pass

            # Create a dummy user with default password
            user = User.objects.create_user(username = "dummy_username", password = "dcx12345")
            user.is_staff = False
            user.is_superuser = False
            user.save()
            # Set new username by using its new ID
            user.username = "NS" + str(user.id)
            user.first_name = dentist_profile_form.cleaned_data['first_name']
            user.last_name = dentist_profile_form.cleaned_data['last_name']
            user.save()

            # User created by admin should be a dentist
            user.dentalclinicuser.role = 'd'
            user.dentalclinicuser.save()

    return redirect('dental_clinic_x:view_dentist_list')

@login_required
@user_passes_test(admin_check, 'dental_clinic_x:index')
def new_dental_service(request):
    template = loader.get_template('new_dental_service.html')
    form = DentalServiceForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(admin_check, 'dental_clinic_x:index')
def create_new_dental_service(request):
    if request.method == 'POST':
        dental_service_form = DentalServiceForm(request.POST)
        if dental_service_form.is_valid():
            dental_service = DentalService()
            dental_service.name = dental_service_form.cleaned_data['name']
            dental_service.price = dental_service_form.cleaned_data['price']
            dental_service.currency = dental_service_form.cleaned_data['currency']
            dental_service.save()

    return redirect('dental_clinic_x:view_dental_service_list')

