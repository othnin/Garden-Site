from django.shortcuts import render, redirect
from django.urls import reverse
import os, datetime, psutil
from .utils import water
from .models import Water


# Create your views here.
def home(request):
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
    water_status = water.get_status()
    auto_water_running = False
    for process in psutil.process_iter():
        try:
            if process.cmdline()[1] == 'pisensors/utils/auto_water.py':
                auto_water_running = True
                break
        except:
            pass

    context = {'waterings': waterings, 'water_status': water_status, 'auto_water_running': auto_water_running}
    return render(request, 'pisensor_home.html', context)


def water_pump_on(request):
    water.pump_on()
    watering = Water(time=datetime.datetime.now(), amount=1)
    watering.save()
    next = request.GET.get('next')
    if next:
        return redirect(next)
    else:
        return redirect(reverse('pisensor_home'))


def auto_water(request, toggle):
    print("Inside auto_water")
    print(toggle)
    if toggle == 'on':
        os.system("python3 pisensors/utils/auto_water.py&")
    else:
        os.system("pkill -f water.py")
    return redirect(reverse('pisensor_home'))