from django.db import models

# Create your models here.
class Doctor(models.Model):
	name = models.CharField(max_length=200)

class Patient(models.Model):
	last_name = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	
class PatientRecord(models.Model):
	patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
	note = models.CharField(max_length=1000)

class Procedure(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	objects = models.Manager()