from django.contrib import admin
from .models import Doctor, Patient, PatientRecord, Procedure

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(PatientRecord)
admin.site.register(Procedure)
