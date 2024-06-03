from django.shortcuts import render
import os
from .utils import water
from .models import Water


# Create your views here.
def home(request):
    print("In pisensors.views.home")
    print(water.get_last_watered())
    path = "../data/last_watered.txt"
    if os.path.isfile(path):    
        with open(path, 'r') as f:
            last_watered = f.read()
            print(last_watered)
            #atering = Water(time= last_watered, amount= 1)
            #watering.save()


    return render(request, 'pisensor_home.html')