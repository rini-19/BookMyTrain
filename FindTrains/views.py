from django.shortcuts import render
from first_app.models import Station, Train

# Create your views here.
def find_view(request):
    if request.method == 'GET':
        src = request.GET.get('src')
        dest = request.GET.get('dest')
        train_list = []
        dept_list = []
        arr_list = []
        src_list = list(Station.objects.filter(station_name = src))
        dest_list = list(Station.objects.filter(station_name = dest))

        for obj1 in src_list:
        	for obj2 in dest_list:
        		if obj1.train_no == obj2.train_no:
        			train_obj = Train.objects.get(train_name = obj1.train_no)
        			train_list.append(train_obj)
        			dept_list.append(obj1.departure_time)
        			arr_list.append(obj2.arrival_time)
        			# train_list.append([obj1.train_no, train_obj.train_name, obj1.departure_time, obj2.arrival_time])

        context = {
        'src' : src,
        'dest': dest,
        'train_list': train_list,
        'dept_list': dept_list,
        'arr_list': arr_list
        }
        return render(request, 'Findtrains/find.html', context)
