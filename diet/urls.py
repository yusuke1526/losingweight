from django.urls import path
from . import views

app_name = 'diet'

urlpatterns = [
    # Diet
    path('add/', views.addmeasured, name='addmeasured'),
]
