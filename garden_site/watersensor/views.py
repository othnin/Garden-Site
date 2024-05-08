from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def home(request):
    print("water_sensor view home")
    return render(request, 'ws_home.html', {})