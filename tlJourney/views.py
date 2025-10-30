from django.shortcuts import render

# Create your views here.
from .models import LearningJourney, AboutMe

def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'index.html', {'experiences': journeys})

def about_me(request):
    profile = AboutMe.objects.first()  # assuming only one record
    return render(request, 'aboutMe.html', {'profile': profile})