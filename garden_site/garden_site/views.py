
import requests, os
from django.shortcuts import render
from weathersensor.models import City, Weather

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid='+os.getenv("OPENWEATHER_KEY")
    cities = City.objects.all() #return all the cities in the database

    weather_data = []
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

    context = {'weather_data' : weather_data}

    return render(request, 'home.html', context)