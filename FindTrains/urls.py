from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^trains/', views.find_view, name='trains'),
]