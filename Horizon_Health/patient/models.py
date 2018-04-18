from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone_number=models.CharField(max_length=256)
    date_of_birth=models.CharField(max_length=256)
    user_id=models.IntegerField()
