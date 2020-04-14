from django.shortcuts import render, get_object_or_404
from account.models import User

def home(request):
    return render(request, 'diet/home.html')

def userpage(request, user_id):
    # the user who have the userpage
    host = get_object_or_404(User, pk=user_id)
    return render(request, 'diet/userpage.html', {'host': host})