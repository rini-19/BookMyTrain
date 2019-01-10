from django.contrib import admin
from .models import Register, Train, Ticket, Station, Passenger
# Register your models here.

admin.site.register(Register)
admin.site.register(Train)
admin.site.register(Ticket)
admin.site.register(Passenger)
admin.site.register(Station)
