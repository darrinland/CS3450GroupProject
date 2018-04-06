from django.urls import path
from . import views


app_name = 'doctor'
urlpatterns = [
	path('', views.index, name='index'),
	path('welcome', views.index, name='index'), 
	path('schedule', views.schedule, name='schedule'),
	path('procedures', views.procedures, name='procedures'),
	path('patients', views.patients, name='patients'),
	path('add_procedure', views.add_procedure, name='add_procedure'),
	path('post_procedure', views.post_procedure, name='post_procedure'),
	path('patient_records/<int:patient_id>', views.patient_records, name='patient_records'),
]
