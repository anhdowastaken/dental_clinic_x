from django import forms

class DentalRecordForm(forms.Form):
    first_name = forms.CharField(label = 'First name', max_length = 100, required = True)
    last_name = forms.CharField(label = 'Last name', max_length = 100, required = True)
    medical_history_operations = forms.BooleanField(label = 'Operations', required = False)
    medical_history_nursing = forms.BooleanField(label = 'Nursing', required = False)
    medical_history_pregnant = forms.BooleanField(label = 'Pregnant', required = False)
    dental_history_bad_breath = forms.BooleanField(label = 'Bad breath', required = False)
    dental_history_sensitive_teeth = forms.BooleanField(label = 'Sensitive teeth', required = False)
