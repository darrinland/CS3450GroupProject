from __future__ import unicode_literals
from django.db import models
from django.apps import apps
from patient.models import Patient



class Appointment(models.Model):
    name = models.CharField(max_length=100, default="not provided")
    phone_num = models.CharField(max_length=20, default="not provided")
    address1 = models.CharField(max_length=50, default="not provided")
    address2 = models.CharField(max_length=50, default="not provided")
    city = models.CharField(max_length=30, default="not provided")
    state = models.CharField(max_length=30, default="not provided")
    zip_code = models.CharField(max_length=20, default="not provided")
    date = models.CharField(max_length=20, default="not provided")
    procedure = models.CharField(max_length=100, default="not provided")
    doctor_name = models.CharField(max_length=100, default="not provided")
    patient_id = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    objects = models.Manager()


