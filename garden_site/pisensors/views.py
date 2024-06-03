from django.shortcuts import render
import os
from .utils import water
from .models import Water


# Create your views here.
def home(request):
    print("In pisensors.views.home")
    path = "pisensors/data/last_watered.txt"
    if os.path.isfile(path):
        with open(path, 'r') as f:
            for line in f:
                elements = line.split()  # Split the line into elements
                if len(elements) >= 2:  # Check if there are at least 2 elements
                    time = " ".join(elements[:-1])  # Join all elements except the last one
                    amount = elements[-1]  # Take the last element
                    watering = Water(time=time, amount=amount)
                    watering.save()
        os.remove(path)
    waterings = Water.objects.all()

    context = {'waterings': waterings}

    return render(request, 'pisensor_home.html', context)
