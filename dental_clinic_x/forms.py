from django import forms

from .models import CURRENCY

class DentalRecordForm(forms.Form):
    first_name = forms.CharField(label = 'First name', max_length = 100, required = True)
    last_name = forms.CharField(label = 'Last name', max_length = 100, required = True)
    medical_history_operations = forms.BooleanField(label = 'Operations', required = False)
    medical_history_nursing = forms.BooleanField(label = 'Nursing', required = False)
    medical_history_pregnant = forms.BooleanField(label = 'Pregnant', required = False)
    dental_history_bad_breath = forms.BooleanField(label = 'Bad breath', required = False)
    dental_history_sensitive_teeth = forms.BooleanField(label = 'Sensitive teeth', required = False)

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

