from django.shortcuts import render, redirect 
from first_app.models import Station, Train
from .forms import TicketForm, PassengerForm
from .models import Ticket, Passenger
import datetime
from datetime import timedelta
import pytz

# Create your views here.
def ticket_view(request):
	psngrcnt = request.POST.get('psngrCnt')
	print(psngrcnt)
	stn_list = Station.objects.values('station_name').distinct()
	pnr_no = 0

	i=0
	if request.method == 'POST':
		form = TicketForm(request.POST or None)
		print('data entered')
		if form.is_valid():
			print('data validated')
			form.save()
			tkt_obj = Ticket.objects.latest('create_time')
			trn_obj = Train.objects.get(train_name = tkt_obj.train_no)
			pnr_no = tkt_obj.pnr
			for i in range(int(psngrcnt)):
				return redirect('psngrData', pnr_no)
				i=i+1
			return redirect('ticketDisplay')
	else:
		form = TicketForm()
	context = {
		'stn_list': stn_list,
		'form': form
	}
	return render(request, 'tickets/ticket_details.html', context)


def passenger_view(request, pnr_no):
	p_name = request.POST.get('name')
	p_age = request.POST.get('age')
	p_gender = request.POST.get('gender')
	if request.method == 'POST':
		form = PassengerForm(request.POST or None)
		if form.is_valid():
			psngr_obj = Passenger.objects.create(pnr_id =pnr_no, name = p_name, age = p_age, gender = p_gender)
			psngr_obj.save()
			if 'addPsngr' in request.POST:
				form = PassengerForm()
			elif 'dispTicket' in request.POST:
				return redirect('ticketDisplay', pnr_no)
	else:
		form = PassengerForm()
	context = {
		'form': form
	}
	return render(request, 'tickets/psngr_details.html', context)

def time_tango(date, time):
    return datetime.datetime.strptime("{}, {}".format(date, time), "%Y-%m-%d, %H:%M:%S")

def display_view(request, pnr_no):
	tkt_obj = Ticket.objects.get(pnr = pnr_no)
	tkt_list = Ticket.objects.all()
	stn_from_obj = Station.objects.get(station_name = tkt_obj.from_station, train_no = tkt_obj.train_no)
	stn_to_obj = Station.objects.get(station_name = tkt_obj.to_station, train_no = tkt_obj.train_no)
	fare = None
	date = tkt_obj.d_o_j
	st = stn_from_obj.departure_time
	et = stn_to_obj.arrival_time 
	tkt_obj.start_time = time_tango(date, st)
	tkt_obj.end_time = time_tango(date, et)
	if stn_to_obj.day > stn_from_obj.day:
		tkt_obj.end_time = tkt_obj.end_time + timedelta(days = 1)

	duration = tkt_obj.end_time - tkt_obj.start_time
	print(duration)
	duration = duration.total_seconds()
	print(duration)
	duration = float(duration/3600)
	print(duration)

	# for obj in tkt_list:
	# 	if obj.end_time is not None and datetime.datetime.now() > obj.end_time:
	# 		obj.delete()

	booked_list = []
	tl = Ticket.objects.filter(coach = tkt_obj.coach)
	QuerySet = Passenger.objects.all()
	for obj in tl:
		for i in QuerySet:
			if i.pnr_id == obj.pnr:
				booked_list.append(i)

	psngr_list = list(Passenger.objects.filter(pnr_id = pnr_no))
	psngrcnt = len(psngr_list)
	trn_obj = Train.objects.get(train_name = tkt_obj.train_no)

	if tkt_obj.coach == 'A':
		fare = trn_obj.fair_A
		tkt_obj.fair = int(trn_obj.fair_A*int(psngrcnt)*duration)
	if tkt_obj.coach == 'B':
		fare = trn_obj.fair_B
		tkt_obj.fair = int(trn_obj.fair_B*int(psngrcnt)*duration)
	if tkt_obj.coach == 'G':
		fare = trn_obj.fair_general
		tkt_obj.fair = int(trn_obj.fair_general*int(psngrcnt)*duration)

	if tkt_obj.coach =='A': 
		a = [0]*trn_obj.coach_A
	if tkt_obj.coach =='B': 
		a = [0]*trn_obj.coach_B
	if tkt_obj.coach =='G': 
		a = [0]*trn_obj.general

	tkt_obj.save()

	for i in range(len(a)):
		for obj in booked_list:
			if obj.seat_no == i:
				a[i] = 1

	for obj in psngr_list:
		for i in range(len(a)):
			if a[i]==0:
				obj.seat_no = i
				a[i] = 1
				obj.status = 'CNF'
				obj.save()
				break

	for obj in psngr_list:
		if obj.seat_no is None:
			obj.status = 'WL'
			obj.save()


	context = {
		'tkt_obj': tkt_obj,
		'psngr_list': psngr_list,
		'trn_obj': trn_obj,
		'fare': fare
		}
	return render(request, 'tickets/ticketDisplay.html', context)

def askTicketDel_view(request):
	pnr_no = request.GET.get('pnr_no')
	if request.method == 'GET' and pnr_no is not None:
		return redirect('tktDel', pnr_no)

	return render(request, 'tickets/askDel.html')

def ticketDelete_view(request, pnr_no):
	tkt_obj = Ticket.objects.get(pnr = pnr_no)
	tkt_obj.delete()

	return render(request, 'tickets/tktDel.html')

def askpnr_view(request):
	pnr_no = request.GET.get('pnr_no')
	if request.method == 'GET' and pnr_no is not None:
		return redirect('pnrDisplay', pnr_no)

	return render(request, 'tickets/askDel.html')

def PNRdisp_view(request, pnr_no):
	tkt_obj = Ticket.objects.get(pnr = pnr_no)
	psngr_list = list(Passenger.objects.filter(pnr_id = pnr_no))
	trn_obj = Train.objects.get(train_name = tkt_obj.train_no)
	fare = None
	if tkt_obj.coach == 'A':
		fare = trn_obj.fair_A
	if tkt_obj.coach == 'B':
		fare = trn_obj.fair_B
	if tkt_obj.coach == 'G':
		fare = trn_obj.fair_general

	context = {
		'tkt_obj': tkt_obj,
		'psngr_list': psngr_list,
		'trn_obj': trn_obj,
		'fare': fare
		}
	return render(request, 'tickets/ticketDisplay.html', context)