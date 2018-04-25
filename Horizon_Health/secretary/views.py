from tempfile import template
from secretary.models import Appointment
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from .models import Appointment

from Login.models import User


# Create your views here.

def index(request):
    template = loader.get_template("secretary/index.html")
    user = User.objects.get(pk=request.session['user_id'])
    return HttpResponse(template.render({ 'user': user }, request))

def create(request):
    template = loader.get_template("secretary/createAppointment.html")
    return HttpResponse(template.render({ 'user': request.session['user_id']}, request))

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
    appoint = Appointment.objects.all()
    context = {'Appointments':appoint}
    return render(request, './secretary/viewAppointment.html', context)

#function to remove the appointment
def delete_appointment(request, id):
    appointDelete = Appointment.objects.get(pk=id)
    appointDelete.delete()
    return redirect('/secretary')

def edit_appointment(request, id):
    appointEdit = Appointment.objects.get(pk=id)
    context = {'item': appointEdit}
    return render(request, './secretary/editAppointment.html', context)

def button_handler(request, id):
    submit_type = request.POST.get('submit_type', None)
    item = Appointment.objects.get(pk=id)
    if submit_type == 'Delete':
        item.delete()
        return redirect('/secretary')
    elif submit_type == 'Edit':
        context = {'item': item}
        return render(request, './secretary/editAppointment.html', context)

def handle_edit(request):
    id = request.POST.get('id')
    item = Appointment.objects.get(pk=id)
    name = request.POST.get('name')
    phone_num =request.POST.get('phone_num')
    address1 = request.POST.get('address1')
    address2 = request.POST.get('address2')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zip_code = request.POST.get('zip_code')
    date = request.POST.get('date')
    item.name = name
    item.phone_num = phone_num
    item.address1 = address1
    item.address2 = address2
    item.city = city
    item.state = state
    item.zip_code = zip_code
    item.date = date
    item.save()
    appoint = Appointment.objects.all()
    context = {'Appointments': appoint}
    return render(request, './secretary/viewAppointment.html', context)


