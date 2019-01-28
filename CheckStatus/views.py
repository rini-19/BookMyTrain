from django.shortcuts import render
from first_app.models import Station

# Create your views here.
def status_view(request):
    route = list(Station.objects.filter(train_no = 23107))
    context = {
      'route': route
    }
    return render(request, 'CheckStatus/status.html', context)