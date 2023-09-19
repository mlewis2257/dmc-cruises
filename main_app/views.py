from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import AddRoomForm, BookingForm
from .models import Cruise, Destination, Booking, User, Excursion
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseServerError
# Create your views here.


def home(request):
    return render(request, 'home.html')


def excursions_index(request):
    excursions = Excursion.objects.all()
    return render(request, 'destinations/detail.html', {'excursions': excursions})


def bookings_index(request):
    bookings = Booking.objects.all()

    # Add destinations to each booking
    for booking in bookings:
        booking.destinations_str = ", ".join(
            [destination.location for destination in booking.cruise.destinations.all()])

    return render(request, 'bookings/index.html', {'bookings': bookings})


def bookings_detail(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    print(booking)
    # id_list = booking.cruise.all().values_list('id')
    add_room_form = AddRoomForm()
    return render(request, 'bookings/detail.html', {
        'booking': booking,
        'add_room_form': add_room_form,
    })


def cruises_index(request):
    cruises = Cruise.objects.all()
    return render(request, 'cruises/index.html', {
        'cruises': cruises
    })


def cruise_detail(request, cruise_id):
    cruise = Cruise.objects.get(id=cruise_id)
    destinations = cruise.destinations.all()
    excursions = Excursion.objects.filter(destination__in=destinations)
    print(excursions)
    return render(request, 'cruises/detail.html', {
        'cruise': cruise,
        'excursions': excursions
    })


def destinations_index(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/index.html', {
        'destinations': destinations
    })


class BookingCreate(CreateView):
    model = Booking
    form_class = BookingForm

    def form_valid(self, form):
        try:
            print(form)
            form.instance.user = self.request.user
            return super().form_valid(form)
        except Exception as e:
            return HttpResponseServerError(e)


class BookingUpdate(UpdateView):
    model = Booking
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookingDelete(DeleteView):
    model = Booking
    success_url = '/bookings'


class BookingList(ListView):
    model = Booking


class BookingDetail(DetailView):
    model = Booking


def destination_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    return render(request, 'destinations/detail.html', {'destination': destination})


def add_room(request, booking_id):
    form = AddRoomForm(request.POST)
    if form.is_valid():
        new_room = form.save(commit=False)
        new_room.booking_id = booking_id
        new_room.save()
    return redirect('detail', booking_id=booking_id)


def assoc_cruise(request, cruise_id, destination_id):
    Cruise.objects.get(id=cruise_id).destinations.add(destination_id)
    return redirect('detail', cruise_id=cruise_id)


def unassoc_cruise(request, cruise_id, destination_id):
    Cruise.objects.get(id=cruise_id).destinations.remove(destination_id)
    return redirect('detail', cruise_id=cruise_id)


def assoc_destination(request, cruise_id, destination_id):
    Cruise.objects.get(id=cruise_id).destinations.add(destination_id)
    return redirect('cruise_detail', cruise_id=cruise_id)


def assoc_user(request, booking_id, user_id):
    User.objects.get(id=user_id).booking.add(booking_id)
    return redirect('bookings/index', user_id=user_id)


def unassoc_user(request, booking_id, user_id):
    User.objects.get(id=user_id).booking.remove(booking_id)
    return redirect('bookings/index', user_id=user_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
