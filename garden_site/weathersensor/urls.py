from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='weathersensor_home'),
    path('deleteCity/<str:id>', views.deleteCity, name='weathersensor_delete_city'),
]