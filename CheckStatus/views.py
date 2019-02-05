from django.http import Http404
from django.shortcuts import render, redirect
from first_app.models import Station, Train
from datetime import time
import datetime
 
# Create your views here.
# def statusForm_view(request):
# 	trainNo = request.GET.get('trainNo')
# 	#return redirect('status',trainNo)
# 	return render(request, 'CheckStatus/statusForm.html')


def status_view(request):
    if request.method == 'GET':
        trainNo = request.GET.get('trainNo')
        train_obj = Train.objects.get(train_no = trainNo )
        route = list(Station.objects.filter(train_no = trainNo ))
        print(route)
        for i in route:
            print(i.id)
        global stn_pass, stn_obj
        global lapse
        c = -1
        time_crrt = datetime.datetime.now().time()
        print(time_crrt)
        for obj in route:
            c = c + 1
            if obj.arrival_time < time_crrt and obj.departure_time > time_crrt:
                stn_pass = 'Train is standing on ' + obj.station_name + ' station'
                break

            if obj.departure_time > time_crrt:
                print(c)
                if c == 0:
                    print(c)
                    stn_pass = 'Train has yet to start'
                    break
                stn_obj = Station.objects.get(id = obj.id - 1)
                stn_pass = 'Train has passed ' + stn_obj.station_name + ' station'
                break
            else:
                stn_pass = 'Train has reached its destination.'
        context = {
          'route': route,
          'stn_pass': stn_pass,
          'train_obj': train_obj
          #'lapse'   : lapse
        }
        return render(request, 'CheckStatus/status.html', context)
