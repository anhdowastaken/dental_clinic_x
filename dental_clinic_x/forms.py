from django import forms

from .models import CURRENCY
from .models import DentalClinicUser
from .models import DentalRecord

class DentalRecordForm(forms.Form):
    first_name = forms.CharField(label = 'First name', max_length = 100, required = True)
    last_name = forms.CharField(label = 'Last name', max_length = 100, required = True)
    medical_history_operations = forms.BooleanField(label = 'Operations', required = False)
    medical_history_nursing = forms.BooleanField(label = 'Nursing', required = False)
    medical_history_pregnant = forms.BooleanField(label = 'Pregnant', required = False)
    dental_history_bad_breath = forms.BooleanField(label = 'Bad breath', required = False)
    dental_history_sensitive_teeth = forms.BooleanField(label = 'Sensitive teeth', required = False)
    dentists = forms.ModelMultipleChoiceField(
        queryset = DentalClinicUser.objects.filter(role__exact = 'd'),
        label = 'Dentists',
        required = True,
    )

class DentistProfileForm(forms.Form):
    first_name = forms.CharField(label = 'First name', max_length = 100, required = True)
    last_name = forms.CharField(label = 'Last name', max_length = 100, required = True)

class DentalServiceForm(forms.Form):
    name = forms.CharField(label = 'Name', max_length = 100, required = True)
    price = forms.CharField(label = 'Price', max_length = 100, required = True)
    currency = forms.ChoiceField(
        label = 'Currency',
        choices = CURRENCY,
        widget = forms.Select(),
        required = True,
    )

class ExaminationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.dental_record_id = kwargs.pop('dental_record_id')
        super(ExaminationForm, self).__init__(*args, **kwargs)

        self.fields['dentist'] = forms.ModelChoiceField(
            queryset = DentalClinicUser.objects.filter(dentists_dentalrecord__id__exact = self.dental_record_id),
            empty_label = None,
            label = 'Dentist',
            required = True,
        )

    note = forms.CharField(
        label = 'Note',
        max_length = 100,
        required = False
    )
    log = forms.CharField(
        label = 'Log',
        max_length = 100,
        required = False
    )

