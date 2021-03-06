from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import User


def registeruser(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['email'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('userpage')
            except IntegrityError:
                return render(request, 'accounts/register.html', {'error': 'That email has already been used.'})

        else:
            return render(request, 'accounts/register.html', {'error': 'Passwords must match.'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    else:
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/login.html', {'error': 'Email or Passwords is wrong.'})
        else:
            login(request, user)
            return redirect('userpage')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
