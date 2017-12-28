from django.urls import path

from . import views

app_name = 'dental_clinic_x'
urlpatterns = [
    path('', views.index, name='index'),
]

