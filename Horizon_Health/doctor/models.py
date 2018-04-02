from django.db import models

# Create your models here.
class Doctor(models.Model):
	name = models.CharField(max_length=200)

class PatientRecord(models.Model):
	doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	note = models.CharField(max_length=1000)
