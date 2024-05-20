from django.db import models

# Create your models here.
from django.utils import timezone
import datetime

#From openweathermap.org APIs
class City(models.Model):
    name = models.CharField(max_length=25)
    lon = models.FloatField(default=0.0)
    lat = models.FloatField(default=0.0)

    def __str__(self): 
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'



class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    main = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    feels_like = models.DecimalField(max_digits=5, decimal_places=2)
    temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    pressure = models.FloatField()
    humidity = models.FloatField()
    visibility = models.FloatField()
    wind_speed = models.FloatField()
    wind_deg = models.DecimalField(max_digits=5, decimal_places=2)
    sunrise = models.CharField(max_length=20)
    sunset = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.city}: {self.temp}°F, {self.description}'




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text