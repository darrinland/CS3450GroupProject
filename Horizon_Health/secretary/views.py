from tempfile import template
from secretary.models import Appointment
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from .models import Appointment


# Create your views here.

def index(request):
    template = loader.get_template("secretary/index.html")
    return HttpResponse(template.render({}, request))

def create(request):
    template = loader.get_template("secretary/createAppointment.html")
    return HttpResponse(template.render({}, request))

def handle_info(request):
    name = request.POST['name']
    phone_num = request.POST['phone_num']
    address1 = request.POST['address1']
    address2 = request.POST['address2']
    city = request.POST['city']
    state = request.POST['state']
    zip_code = request.POST['zip_code']
    date = request.POST['date']
    appointment = Appointment(name = name, phone_num = phone_num, address1 = address1, address2 = address2, city = city, state = state, zip_code = zip_code, date = date)
    appointment.save()
    return redirect('/secretary')

def viewAppointment(request):
    appoint =Appointment.objects.all()
    context = {'Appointments':appoint}
    return render(request, './secretary/viewAppointment.html', context)



