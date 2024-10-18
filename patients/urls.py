from django.urls import path
from . import views

urlpatterns = [
     path('', views.landing_page, name='landing_page'),
    path('register/', views.register_patient, name='register_patient'),
    path('search/', views.search_patient, name='search_patient'),
    path('list/', views.view_patients, name='view_patients'),
    path('success/<int:patient_id>/', views.success, name='patient_success'),
    path('success/<int:patient_id>/', views.success, name='patient_success'),

]
