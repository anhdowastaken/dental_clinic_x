from django.urls import path
from django.urls import include

from . import views

app_name = 'dental_clinic_x'
urlpatterns = [
    path('', views.index, name='index'),
    # Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_new_dental_record/', views.create_new_dental_record, name="create_new_dental_record"),
    path('view_dental_record/<int:record_id>/', views.view_dental_record, name="view_dental_record"),
]

