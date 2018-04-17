from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import User
from patient.models import Patient

def index(request):
	return render(request, 'Login/index.html')

def newUser(request):
	return render(request, 'Login/newUser.html')

def handleLogin(request):
	user = User.objects.filter(user_name=request.POST['user_name'], password=request.POST['password']).first()
	if user:
		if user.userType == "patient":
			return redirect('http://127.0.0.1:8000/patient?user='+str(user.pk))
		elif user.userType == "doctor":
			return redirect('http://127.0.0.1:8000/doctor?user='+str(user.pk))
		elif user.userType == "secretary":
			return redirect('http://127.0.0.1:8000/secretary?user='+str(user.pk))
	else:
		return redirect('Login:failedLogin')

def handleNewUser(request):
	user = User(user_name=request.POST['user_name'], password=request.POST['password'], userType='patient')
	user.save()
	patient = Patient()
	patient.save()
	return redirect('http://127.0.0.1:8000/patient/?user='+str(user.pk))

def failedLogin(request):
	return HttpResponse("Login Failed.  Please go back and try again.")
