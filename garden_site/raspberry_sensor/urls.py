from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='raspberry_sensor_home'),
    path('sensor/',views.sensor, name='sensor')
]