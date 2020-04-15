from django.urls import path
from . import views

app_name = 'measured'

urlpatterns = [
    # Diet
    path('add/', views.add, name='add'),
]
