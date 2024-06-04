from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='pisensor_home'),
    path('pump_on/', views.water_pump_on, name='water_pump_on'),
    path('auto_water/<str:toggle>/', views.auto_water, name='auto_water'),
]