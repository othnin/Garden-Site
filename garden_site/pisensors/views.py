from django.shortcuts import render
import os
from .utils import water


# Create your views here.
def home(request):
    print("In pisensors.views.home")
    print(water.get_last_watered())
    return render(request, 'pisensor_home.html')