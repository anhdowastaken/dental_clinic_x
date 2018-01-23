from django.urls import path
from django.urls import include

from . import views

app_name = 'dental_clinic_x'
urlpatterns = [
    path('', views.index, name='index'),
    # Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),

    path('view_dental_record_list/', views.view_dental_record_list, name="view_dental_record_list"),
    path('view_dental_record/<int:record_id>/', views.view_dental_record, name="view_dental_record"),
    path('new_dental_record/', views.new_dental_record, name="new_dental_record"),
    path('create_new_dental_record/', views.create_new_dental_record, name="create_new_dental_record"),
    path('delete_dental_record/', views.delete_dental_record, name="delete_dental_record"),

    path('view_dentist_list/', views.view_dentist_list, name="view_dentist_list"),
    path('view_dentist/<int:dentist_id>/', views.view_dentist, name="view_dentist"),
    path('new_dentist_profile/', views.new_dentist_profile, name="new_dentist_profile"),
    path('create_new_dentist_profile/', views.create_new_dentist_profile, name="create_new_dentist_profile"),
    path('delete_dentist_profile/', views.delete_dentist_profile, name="delete_dentist_profile"),

    path('view_dental_service_list/', views.view_dental_service_list, name="view_dental_service_list"),
    path('view_dental_service/<int:service_id>/', views.view_dental_service, name="view_dental_service"),
    path('new_dental_service/', views.new_dental_service, name="new_dental_service"),
    path('create_new_dental_service/', views.create_new_dental_service, name="create_new_dental_service"),
    path('delete_dental_service/', views.delete_dental_service, name="delete_dental_service"),

    path('new_examination/<int:record_id>/', views.new_examination, name="new_examination"),
    path('create_new_examination/<int:record_id>/', views.create_new_examination, name="create_new_examination"),
]

