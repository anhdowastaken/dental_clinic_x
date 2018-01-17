from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from .models import DentalRecord
from .forms import DentalRecordForm

def admin_check(user):
    if user.is_authenticated:
        return user.dentalclinicuser.is_admin()
    else:
        return False

def dentis_check(user):
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
        form = DentalRecordForm()
        context = {
            'dental_records': dental_records,
            'form': form,
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
            user.username = "patient" + str(user.id)
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
