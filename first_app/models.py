from __future__ import unicode_literals
from django.db import models


GENDER = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('O', 'Other'),
)
# Create your models here.
class Register(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER)
    dob = models.DateField()
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    #varify_password = models.CharField(max_length=15)


class Train(models.Model):
    train_no = models.IntegerField(primary_key=True)
    train_name = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    coach_A = models.IntegerField()
    coach_B = models.IntegerField()
    general = models.IntegerField()
    fair_A = models.IntegerField()
    fair_B = models.IntegerField()
    fair_general = models.IntegerField()

    def __unicode__(self):
        return self.train_name

    def __str__(self):
        return self.train_name


class Station(models.Model):
    station_name = models.CharField(max_length=30)
    train_no = models.ForeignKey( Train, on_delete=models.CASCADE)
    # arival_time = models.CharField(max_length=30, null = True)
    # depetrure_time = models.CharField(max_length=30, null = True)
    arrival_time = models.TimeField(null = True)
    departure_time = models.TimeField(null = True)
    platform = models.IntegerField()
    day = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.station_name

    def __str__(self):
        return self.station_name






