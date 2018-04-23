from __future__ import unicode_literals
from django.db import models
from django.apps import apps
from patient.models import Patient



class Appointment(models.Model):
    name = models.CharField(max_length=100, default="null")
    phone_num = models.CharField(max_length=20, default="null")
    address1 = models.CharField(max_length=50, default="null")
    address2 = models.CharField(max_length=50, default="null")
    city = models.CharField(max_length=30, default="null")
    state = models.CharField(max_length=30, default="null")
    zip_code = models.CharField(max_length=20, default="null")
    date = models.CharField(max_length=20, default="null")
    procedure = models.CharField(max_length=100, default="null")
    doctor_name = models.CharField(max_length=100, default="null")
    patient_id = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    objects = models.Manager()


