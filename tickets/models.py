from __future__ import unicode_literals
from django.db import models
from first_app.models import Train

GENDER = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('O', 'Other'),
)

COACH = (
	('A', 'first class'),
	('B', 'Second class'),
	('G', 'general')
)

# Create your models here.
class Ticket(models.Model):
	pnr = models.IntegerField(primary_key=True)
	create_time = models.DateTimeField(auto_now_add = True)
	train_no = models.ForeignKey(Train, on_delete=models.CASCADE)
	coach = models.CharField(choices = COACH, default = 'G', max_length = 1)
	from_station = models.CharField(max_length=30)
	to_station = models.CharField(max_length=30)
	fair = models.IntegerField(null = True)
	d_o_j = models.DateField()
	start_time = models.DateTimeField(null = True)
	end_time = models.DateTimeField(null = True)


class Passenger(models.Model):
	pnr = models.ForeignKey(Ticket, on_delete = models.CASCADE)
	name = models.CharField(max_length = 30)
	age = models.IntegerField()
	gender = models.CharField(choices = GENDER, default = 'F', max_length = 1)
	seat_no = models.IntegerField(null = True)
	status = models.CharField(max_length = 3, null = True)
		