from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from .forms import DentalRecordForm

def index(request):
    template = loader.get_template('index.html')
    form = DentalRecordForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def create_new_dental_record(request):
    if request.method == 'POST':
        form = DentalRecordForm(request.POST)
        print(request.POST)
    else:
        print('method is GET')
        return redirect('dental_clinic_x:index')

