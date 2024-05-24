from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='weathersensor_home'),
    path('deleteCity/<str:city_name>', views.deleteCity, name='weathersensor_delete_city'),
    path('getWeatherTemps/<str:city_name>', views.getWeatherTempData, name='weathersensor_get_weather_temps'),
    path('getWeatherData/<str:city_name>', views.getWeatherMostData, name='weathersensor_get_weather_data')
]