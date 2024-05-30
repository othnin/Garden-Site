from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def home(request):
    print("raspberry_sensor view home")
    return render(request, 'raspberry_sensor_home.html', {})

def sensor(request):

    return render(request, "sensor.html", {
        'sensor': '99',
    })