from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'collegehub/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = RegisterForm()
    return render(request, 'collegehub/login.html')


@login_required(login_url="/login/")
def home_view(request):
    return render(request, 'collegehub/home.html')