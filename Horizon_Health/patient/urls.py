from django.urls import path
from . import views

app_name = 'patient'
urlpatterns = [
        path('', views.index, name='index'),
        path('settings', views.settings, name='settings'),
        path('appointment', views.appointment, name='appointment'),
        path('update_patient/<int:patient_id>', views.update_patient, name='update_patient'),
]


