from django.shortcuts import render
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,
)

from .forms import userLoginForm

# Create your views here.
def login_view(request):
    title = "login"
    form = userLoginForm(request.POST or none)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    return render(request, "index.html", {"form":form, "title":title})

def register_view(request):
    return render(request, "", {})

def logout_view(request):
    return render(request, "", {})
