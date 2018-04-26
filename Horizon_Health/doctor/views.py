from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, request
from django.template import loader
from .models import Patient, Procedure, PatientRecord

from Login.models import User

def index(request):
	template = loader.get_template('doctor/index.html')
	user = User.objects.get(pk=request.session['user_id'])
	return HttpResponse(template.render({ 'user': user }, request))

def schedule(request):
	template = loader.get_template('doctor/schedule.html')
	user = User.objects.get(pk=request.session['user_id'])
	return HttpResponse(template.render({ 'user': user }, request))

def procedures(request):
	procedure_list = Procedure.objects.order_by('id')
	user = User.objects.get(pk=request.session['user_id'])
	context = {'procedure_list': procedure_list,  'user': user }
	return render(request, 'doctor/procedures.html', context)

def add_procedure(request):
	template = loader.get_template('doctor/add_procedure.html')
	user = User.objects.get(pk=request.session['user_id'])
	return HttpResponse(template.render({ 'user': user }, request))

def post_procedure(request):
	name = request.POST['name']
	description = request.POST['description']
	proc = Procedure(name = name, description = description)
	proc.save()
	return redirect('/doctor/procedures')

def patients(request):
	patient_list = Patient.objects.order_by('id')
	user = User.objects.get(pk=request.session['user_id'])
	context = {'patient_list': patient_list,  'user': user }
	return render(request, 'doctor/patients.html', context)

def patient_records(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	patientRecord = PatientRecord.objects.filter(patient_id=patient)
	user = User.objects.get(pk=request.session['user_id'])
	context = {'patient': patient, 'records': patientRecord,  'user': user }
	return render(request, 'doctor/patient_records.html', context)
def new_record(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	user = User.objects.get(pk=request.session['user_id'])
	context = {'patient': patient,  'user': user }
	return render(request, 'doctor/new_record.html', context)
def add_new_record(request, patient_id):
	patient = Patient.objects.get(pk=patient_id)
	record = PatientRecord()
	record.patient_id = patient
	record.note = request.POST.get('note', False)
	record.save()
	return redirect('/doctor/patients/patient_records')

def delete_procedure(request, id):
	pro = Procedure.objects.get(pk=id)
	pro.delete()
	return redirect('/doctor/procedures')
