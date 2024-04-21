from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User 
from .forms import SignupForm, LogoutForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def create_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request, customer)
            return redirect('store')
        else:
            messages.error(request, form.errors)
    else:
        form = SignupForm()
    context = {'form':form}
    return render(request, 'signup.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('store')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('store')
        else:
            messages.error(request, form.errors)
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login_page.html', context)

def logout_view(request):
    if request.method == 'POST':
        form = LogoutForm(request.POST)
        if form.is_valid():
            logout(request)
            messages.success(request, 'You have been logged out!')
            return redirect('store')
        else:
            form = LogoutForm()
        context = {'form':form}
        return render(request, 'login_page.html', context)
    
def password_reset(request):
    pass