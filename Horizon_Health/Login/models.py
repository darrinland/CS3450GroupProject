from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=30)
    pass_word = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=30)
    pass_word = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Secretary(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=30)
    pass_word = models.CharField(max_length=30)
    def __str__(self):
        return self.name
