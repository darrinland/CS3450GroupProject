from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('welcome', views.index, name='index'), 
	path('schedule', views.schedule, name='schedule'),
	path('procedures', views.procedures, name='procedures'),
	path('patients', views.patients, name='patients'),
]