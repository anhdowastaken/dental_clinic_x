from django.urls import path
from django.urls import include

from . import views

app_name = 'dental_clinic_x'
urlpatterns = [
    path('', views.index, name='index'),
    # Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
]

