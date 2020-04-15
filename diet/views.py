from django.shortcuts import render, get_object_or_404
from accounts.models import User

def home(request):
    return render(request, 'diet/home.html')

def userpage(request):
    return render(request, 'diet/userpage.html')