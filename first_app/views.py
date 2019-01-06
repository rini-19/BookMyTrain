from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def index(request):
    return render(request, 'first_app/index.html')

def user(request):
    return render(request, 'first_app/userDashboard.html')

def Register_view(request):
    form = forms.Register()

    if request.method == 'POST':
        form = forms.Register(request.POST)

        if form.is_valid():
            #do some code
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("USERNAME: " + form.cleaned_data['username'])
            print("PASSWORD: " + form.cleaned_data['password'])
            print("VARIFY_PASSWORD: " + form.cleaned_data['varify_password'])




    return render(request, 'first_app/form_page.html', {'form':form})
