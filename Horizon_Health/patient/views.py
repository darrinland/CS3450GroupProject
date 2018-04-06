from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .models import Patient

# Create your views here.

def index(request) :
    patients = Patient.objects.get(pk=1)
    req = {
        'patients': patients
    }
    template=loader.get_template("patient/index.html")
    return HttpResponse(template.render(req, request))

def settings(request) :
    patients = Patient.objects.get(pk=1)
    req = {
        'patients': patients
    }
    template=loader.get_template("patient/settings.html")
    return HttpResponse(template.render(req, request))

def appointment(request) :
    patients = Patient.objects.get(pk=1)
    req = {
        'patients': patients
    }
    template=loader.get_template("patient/appointment.html")
    return HttpResponse(template.render(req, request))

def update_patient(request, patient_id) :
    patient = Patient.objects.get(pk=patient_id)
    patient.first_name = request.POST.get('firstname', False)
    patient.last_name = request.POST.get('lastname', False)
    patient.date_of_birth = request.POST.get('dob', False)
    patient.phone_number = request.POST.get('phone_number', False)
    patient.save()
    return redirect('/patient')
