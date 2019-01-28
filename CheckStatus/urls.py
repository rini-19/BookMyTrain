from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^status/', views.status_view, name='status'),
]