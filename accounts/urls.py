from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Auth
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registeruser, name='register'),
]
