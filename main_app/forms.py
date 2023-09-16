from django.forms import ModelForm
from .models import Room


class BookingForm(ModelForm):
    class Meta:
        model = Room
        fields = ['type', 'number', 'location']
