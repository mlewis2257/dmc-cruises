from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cruise, Destination, Booking

# Create your views here.


def home(request):
    return render(request, 'home.html')


def cruises_index(request):
    cruises = Cruise.objects.all()
    return render(request, 'cruises/index.html', {
        'cruises': cruises
    })


def cruise_detail(request, cruise_id):
    cruise = Cruise.objects.get(id=cruise_id)
    return render(request, 'cruises/detail.html', {'cruise': cruise})


def destinations_index(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/index.html', {
        'destinations': destinations
    })


class BookingCreate(CreateView):
    model = Booking
    fields = '__all__'
