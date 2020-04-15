from django.urls import path
from . import views

app_name = 'diet'

urlpatterns = [
    # Diet
    path('add/measured/', views.addmeasured, name='addmeasured'),
    path('add/diet', views.adddiet, name='adddiet'),
]
