from django.urls import path
from . import views

app_name = 'Login'

urlpatterns = [
	path('', views.index, name='index'),
	path('handleLogin/', views.handleLogin, name='handleLogin'),
	path('new-user/', views.newUser, name='newUser'),
	path('handleNewUser/', views.handleNewUser, name='handleNewUser'),
	path('failedLogin/', views.failedLogin, name='failedLogin'),
	path('handleLogout/', views.handleLogout, name='handleLogout'),
]
