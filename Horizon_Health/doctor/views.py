from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Patient, Procedure

def index(request):
	template = loader.get_template('doctor/index.html')
	return HttpResponse(template.render({}, request))

def schedule(request):
	template = loader.get_template('doctor/schedule.html')
	return HttpResponse(template.render({}, request))
	
def procedures(request):
	procedure_list = Procedure.objects.order_by('id')
	context = {'procedure_list': procedure_list}
	return render(request, 'doctor/procedures.html', context)

def add_procedure(request):
	template = loader.get_template('doctor/add_procedure.html')
	return HttpResponse(template.render({}, request))

def post_procedure(request):
	name = request.POST['name']
	description = request.POST['description']
	proc = Procedure(name = name, description = description)
	proc.save()
	return redirect('/doctor/procedures')
	
def patients(request):
	patient_list = Patient.objects.order_by('id')
	context = {'patient_list': patient_list}
	return render(request, 'doctor/patients.html', context)

def patient_records(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	context = {'patient': patient}
	return render(request, 'doctor/patient_records.html', context)
