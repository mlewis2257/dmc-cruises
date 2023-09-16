from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cruise, Destination

# Create your views here.


def home(request):
    return render(request, 'home.html')


def cruises_index(request):
    cruises = Cruise.objects.all()
    return render(request, 'cruises/index.html', {
        'cruises': cruises
    })


def destinations_index(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/index.html', {
        'destinations': destinations
    })
