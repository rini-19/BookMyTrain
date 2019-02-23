from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.login_view , name='index'),
    url(r'^registerpage/', views.register_view, name='registerpage'),
    url(r'^userDashboard/',views.user, name='userdashboard'),
]
