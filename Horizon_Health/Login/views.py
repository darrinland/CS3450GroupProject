from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import User
from patient.models import Patient
from patient.urls import urlpatterns
from doctor.urls import urlpatterns
from secretary.urls import urlpatterns

def index(request):
	return render(request, 'Login/index.html')

def newUser(request):
	return render(request, 'Login/newUser.html')

def handleLogin(request):
	user = User.objects.filter(user_name=request.POST['user_name'], password=request.POST['password']).first()
	if user:
		request.session['user_id'] = str(user.pk)
		if user.userType == "patient":
			return redirect('patient:index')
		elif user.userType == "doctor":
			return redirect('doctor:index')
		elif user.userType == "secretary":
			return redirect('secretary:index')
	else:
		return redirect('Login:failedLogin')

def handleNewUser(request):
	user = User(user_name=request.POST['user_name'], password=request.POST['password'], userType='patient')
	user.save()
	patient = Patient(first_name="12", last_name="Thompson", date_of_birth="may", user_id=str(user.pk))
	patient.save()
	request.session['user_id'] = str(user.pk)
	return redirect('patient:index')

def failedLogin(request):
	return HttpResponse("Login Failed.  Please go back and try again.")

def handleLogout(request):
	request.session.flush()
	return redirect('Login:index');
