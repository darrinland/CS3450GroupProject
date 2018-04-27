from django.urls import path
from . import views


app_name = 'doctor'
urlpatterns = [
	path('', views.index, name='index'),
	path('welcome', views.index, name='index'),
	path('procedures', views.procedures, name='procedures'),
	path('patients', views.patients, name='patients'),
	path('add_procedure', views.add_procedure, name='add_procedure'),
	path('post_procedure', views.post_procedure, name='post_procedure'),
	path('patient_records/<int:patient_id>', views.patient_records, name='patient_records'),
	path('patient_records/new_record/<int:patient_id>', views.new_record, name='new_record'),
	path('add_new_record/<int:patient_id>', views.add_new_record, name='add_new_record'),
	path('deleteProcedure/<int:id>/delete/', views.delete_procedure, name='deleteProcedure'),
]
