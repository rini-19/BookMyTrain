from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Register(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.IntegerField()
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    varify_password = models.CharField(max_length=15)

 
