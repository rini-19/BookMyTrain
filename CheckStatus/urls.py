from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^getTrain/', views.statusForm_view, name='getTrain'),
    url(r'^status/', views.status_view, name='status'),
]