from django.shortcuts import render
from accounts.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'diet/home.html')

@login_required
def userpage(request):
    return render(request, 'diet/userpage.html')