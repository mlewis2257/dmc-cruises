from django.forms import ModelForm
from .models import Room


class BookingForm(ModelForm):
    class Meta:
        model = Room
        fields = ['type', 'number', 'location']

class AddRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'