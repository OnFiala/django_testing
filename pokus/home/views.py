from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()          # uloží uživatele do DB
            login(request, user)        # rovnou ho přihlásí
            return redirect("home")     # po registraci -> home
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def home(request):
    return render(request, "home.html")

@login_required
def info(request):
    return render(request, "info.html")

