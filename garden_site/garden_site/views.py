
from django.shortcuts import render


def home(request):
    print("garden_site home view")
    return render(request, 'home.html', {})