from django.forms import ModelForm
from .models import Room, Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        # fields = ['type', 'number', 'location']
        exclude = ['user']

class AddRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
