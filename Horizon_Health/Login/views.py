from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
	return render(request, 'Login/index.html')

def handleLogin(request):
	return redirect('http://127.0.0.1:8000/patient/')
