from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum
from datetime import datetime
from accounts.models import User
from diet.models import Diet
from measured.models import Measured

def home(request):
    return render(request, 'diet/home.html')

@login_required
def userpage(request):
    diets = Diet.objects.filter(user=request.user, date=timezone.now())
    try:
        measured = Measured.objects.get(user=request.user, measured_date=timezone.now())
    except Measured.DoesNotExist:
        measured = None
    calorie__sum = diets.aggregate(Sum('calorie'))['calorie__sum']
    return render(request, 'diet/userpage.html', {'diets': diets, 'calorie__sum': calorie__sum, 'measured': measured})

@login_required
def add(request):
    if request.method == 'GET':
        return render(request, 'diet/add.html')
    else:
        try:
            date = datetime.strptime(request.POST['date'], '%Y-%m-%d')
        except ValueError:
            return render(request, 'diet/add.html', {'error': 'Format of date is not proper.'})
        diet = Diet(name=request.POST['name'], calorie=request.POST['calorie'], date=request.POST['date'], user=request.user)
        diet.save()
        return redirect('userpage')