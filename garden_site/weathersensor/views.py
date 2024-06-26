import requests, os
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse

from .models import City, Weather
from .forms import CityForm


def home(request):
    city_deleted = request.GET.get('deleted', False)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid='+os.getenv("OPENWEATHER_KEY")
    cities = City.objects.all() #return all the cities in the database
    city_names = [city.name for city in cities]

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            # Check if the city already exists in the database
            if not City.objects.filter(name__iexact=city_name).exists():
                form.save()
    else:
        form = CityForm()

    weather_data = []
    if cities.exists():
        for city in cities:
            city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
            weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
            }
            weather_data.append(weather) #add the data for the current city into our list for display
            w = Weather(city=city, main= city_weather['weather'][0]['main'], temp=city_weather['main']['temp'],
                                description=city_weather['weather'][0]['description'], feels_like=city_weather['main']['feels_like'],
                                temp_min=city_weather['main']['temp_min'], temp_max=city_weather['main']['temp_max'],
                                pressure=city_weather['main']['pressure'], humidity=city_weather['main']['humidity'],
                                visibility=city_weather['visibility'], wind_speed=city_weather['wind']['speed'],
                                wind_deg=city_weather['wind']['deg'], sunrise = city_weather['sys']['sunrise'], sunset = city_weather['sys']['sunset']
                                )
            w.save()

    context = {'weather_data' : weather_data, 'form' : form, 'city_names': city_names}
    return render(request, 'weathersensor_home.html', context)


def deleteCity(request, city_name=None):
    try:
        city = City.objects.get(name=city_name)
    except City.DoesNotExist:
        return redirect('weathersensor_home')
    city.delete()
    cities = City.objects.all() 
    weather_data = []
    for city in cities:
        weather = {
            'city': city.name,
            'temperature' : city.weather_set.last().temp,
            'description' : city.weather_set.last().description,
        }
        weather_data.append(weather)

    context = {'weather_data' : weather_data}
    return redirect(reverse('weathersensor_home') + '?deleted=true')  #may not need URL parameters


def getWeatherTempData(request, city_name):
    # Get the city object based on the city name
    city = get_object_or_404(City, name=city_name)
    # Perform the query to get weather data for the specified city
    weather_data = Weather.objects.filter(city=city).values('temp', 'time')
    # Convert the queryset to a list
    data = list(weather_data)
    return JsonResponse(data, safe=False)
        

def getWeatherMostData(request, city_name):
    # Get the city object based on the city name
    city = get_object_or_404(City, name=city_name)
    # Perform the query to get weather data for the specified city
    weather_data = Weather.objects.filter(city=city).values('time','temp', 'feels_like', 'temp_min','temp_max', 'humidity','wind_speed','description')
    # Convert the queryset to a list
    data = list(weather_data)
    return JsonResponse(data, safe=False)

