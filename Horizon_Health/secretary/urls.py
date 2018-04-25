from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'secretary'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('#', views.handle_info, name='handle_info'),
    path('viewAppointment', views.viewAppointment, name='viewAppointment'),
    path('appointment/<int:id>/delete/', views.delete_appointment, name='deleteAppointment'),
    path('editAppointment', views.handle_edit, name='handle_edit'),
    path('appointment/<int:id>/edit/', views.button_handler, name='buttonHandler'),


]


