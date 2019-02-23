from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^ticketData/', views.ticket_view, name='ticketData'),
    url(r'^psngrData/(?P<pnr_no>\d+)/', views.passenger_view, name='psngrData'),
    url(r'^ticketDisplay/(?P<pnr_no>\d+)/', views.display_view, name='ticketDisplay'),
    url(r'^askDel/', views.askTicketDel_view, name='askDel'),
    url(r'^tktDel/(?P<pnr_no>\d+)/', views.ticketDelete_view, name='tktDel'),
    url(r'^askPNR/', views.askpnr_view, name='askPNR'),
    url(r'^pnrDisplay/(?P<pnr_no>\d+)/', views.PNRdisp_view, name='pnrDisplay'),
]