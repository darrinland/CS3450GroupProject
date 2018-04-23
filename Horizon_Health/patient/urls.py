from django.urls import path
from . import views

app_name = 'patient'
urlpatterns = [
        path('', views.index, name='index'),
        path('settings', views.settings, name='settings'),
        path('appointment', views.appointment, name='appointment'),
        path('add_appointment', views.add_appointment, name='add_appointment'),
        path('save_appointment', views.save_appointment, name='save_appointment'),
        path('update_patient/<int:patient_id>', views.update_patient, name='update_patient'),
        path('delete_appointment/<int:appointment_id>', views.delete_appointment, name='delete_appointment'),
]


