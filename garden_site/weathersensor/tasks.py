
#from celery import shared_task
#from weathersensor.celery import app
from celery import shared_task
from .models import Weather, City
import requests, os

@shared_task
def fetch_and_save_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid='+os.getenv("OPENWEATHER_KEY")
    cities = City.objects.all()
    for city in cities:

        city_weather = requests.get(url.format(city)).json()
    

        w = Weather(city=city, main= city_weather['weather'][0]['main'], temp=city_weather['main']['temp'],
                            description=city_weather['weather'][0]['description'], feels_like=city_weather['main']['feels_like'],
                            temp_min=city_weather['main']['temp_min'], temp_max=city_weather['main']['temp_max'],
                            pressure=city_weather['main']['pressure'], humidity=city_weather['main']['humidity'],
                            visibility=city_weather['visibility'], wind_speed=city_weather['wind']['speed'],
                            wind_deg=city_weather['wind']['deg'], sunrise = city_weather['sys']['sunrise'], sunset = city_weather['sys']['sunset']
                            )
        w.save()