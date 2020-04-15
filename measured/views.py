from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def add(request):
    return render(request, 'diet/add.html')
