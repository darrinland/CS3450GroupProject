from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from doctor.models import Procedure

from .models import Patient
from Login.models import User
from django.apps import apps
Appointment = apps.get_model('secretary', 'Appointment')
# Create your views here.

def index(request) :
    patients = Patient.objects.get(user_id=request.session['user_id'])
    user = User.objects.get(pk=request.session['user_id'])
    req = {
        'patients': patients,
        'user' : user,
    }
    template=loader.get_template("patient/index.html")
    return HttpResponse(template.render(req, request))

def settings(request) :
    patients = Patient.objects.get(user_id=request.session['user_id'])
    user = User.objects.get(pk=request.session['user_id'])
    req = {
        'patients': patients,
        'user' : user,
    }
    template=loader.get_template("patient/settings.html")
    return HttpResponse(template.render(req, request))

def appointment(request) :
    patient = Patient.objects.get(user_id=request.session['user_id'])
    user = User.objects.get(pk=request.session['user_id'])
    appointment_list = Appointment.objects.filter(patient_id=patient)
    req = {
        'appointments': appointment_list,
        'user' : user,
    }
    template=loader.get_template("patient/appointment.html")
    return HttpResponse(template.render(req, request))

def update_patient(request, patient_id) :
    patient = Patient.objects.get(user_id=patient_id)
    patient.first_name = request.POST.get('firstname', False)
    patient.last_name = request.POST.get('lastname', False)
    patient.date_of_birth = request.POST.get('dob', False)
    patient.phone_number = request.POST.get('phone_number', False)
    patient.save()
    return redirect('/patient')
def add_appointment(request) :
    template=loader.get_template("patient/add_appointment.html")
    return HttpResponse(template.render({}, request))
def save_appointment(request) :
    patient = Patient.objects.get(user_id = request.session['user_id'])
    appointment = Appointment()
    appointment.patient_id = patient
    appointment.date = request.POST.get('date', False)
    appointment.procedure = request.POST.get('procedure', False)
    appointment.doctor_name = request.POST.get('doctor_name', False)
    appointment.save()
    return redirect('/patient')
def delete_appointment(request, appointment_id) :
    Appointment.objects.get(pk=appointment_id).delete()
    return redirect('/patient/appointment')

def viewProcedure(request):
    return redirect('/doctor/procedures')
