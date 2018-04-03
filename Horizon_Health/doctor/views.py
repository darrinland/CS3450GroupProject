from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('doctor/index.html')
	return HttpResponse(template.render({}, request))

def schedule(request):
	template = loader.get_template('doctor/schedule.html')
	return HttpResponse(template.render({}, request))
	
def procedures(request):
	template = loader.get_template('doctor/procedures.html')
	return HttpResponse(template.render({}, request))

def patients(request):
	template = loader.get_template('doctor/patients.html')
	return HttpResponse(template.render({}, request))
