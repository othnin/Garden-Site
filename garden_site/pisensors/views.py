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
            for line in f:
                elements = line.split()  # Split the line into elements
                if len(elements) >= 2:  # Check if there are at least 2 elements
                    time = elements[0]
                    amount = elements[1]
                    watering = Water(time=time, amount=amount)
                    watering.save()
        os.remove(path)
    waterings = Water.objects.all()
    context = {'waterings': waterings}

    return render(request, 'pisensor_home.html', context)