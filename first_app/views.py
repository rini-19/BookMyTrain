from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model, login, logout 

from .forms import userLoginForm, RegisterForm


def index(request):
    return render(request, 'first_app/index.html')

def user(request):
    return render(request, 'first_app/userDashboard.html')

def login_view(request):
    print(request.user.is_authenticated)
    form = userLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user= authenticate(username = username, password =password)
        login(request, user)
        return redirect('userdashboard')
    return render(request, "first_app/index.html", {"form":form})

def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        print("VALIDATION SUCCESS!")
        instance = form.save(commit = False)
        password = form.cleaned_data.get("password")
        instance.set_password(password)
        instance.save()
        new_user= authenticate(username = instance.username, password =password)
        login(request, new_user)
        return redirect('userdashboard')
            #instance.save()

    #    else:
    return render(request, 'first_app/form_page.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect(request, reverse('index'))

