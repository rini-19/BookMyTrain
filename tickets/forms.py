from django import forms 
from django.forms import ModelForm
from first_app.models import Train, Station
from .models import Ticket, Passenger

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

class TicketForm(forms.ModelForm):
	psngrCnt = forms.IntegerField()
	coach = forms.ChoiceField(choices = COACH)
	d_o_j = forms.DateField(widget = forms.DateInput())
	# from_station = forms.ChoiceField(choices = stn_list)
	def __init__(self, *args, **kwargs):
		super(TicketForm, self).__init__(*args, **kwargs)
		stn_list = []
		for obj in Station.objects.values('station_name').distinct():
			stn_list.append(obj)
		self.fields['from_station'] = forms.ChoiceField(
			choices=[(o['station_name'], o['station_name']) for o in stn_list]
		)
		self.fields['to_station'] = forms.ChoiceField(
			choices=[(o['station_name'], o['station_name']) for o in stn_list]
		)
	
	class Meta:
		model = Ticket
		fields = [
			'train_no',
			'from_station',
			'to_station',
			'd_o_j',
			'coach',
			'psngrCnt'
			]

class PassengerForm(forms.ModelForm):
	gender= forms.ChoiceField(choices = GENDER)
	class Meta:
		model = Passenger
		fields = [
			'name',
			'age',
			'gender'
			]
	
	
		