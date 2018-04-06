# Generated by Django 2.0.2 on 2018-04-03 20:25

from django.db import migrations

def add_patients(apps, schema_editor):
    Patient = apps.get_model('patient', 'Patient')
    patient = Patient(first_name='Ani',
                      last_name='Park',
                      phone_number='4352596587',
                      date_of_birth='02-05-1975')
    patient.save()


    patient = Patient(first_name='Anna',
                      last_name='Simpson',
                      phone_number='4513121132',
                      date_of_birth='02-05-1985')
    patient.save()


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_patients)
    ]