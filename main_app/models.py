import datetime
from django.db import models
from django.urls import reverse
from django.db.models import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

TYPE = (
    ('I', 'Interior'),
    ('O', 'Ocean View'),
    ('B', 'Balcony'),
    ('JS', 'Junior Suite'),
    ('S', 'Suite'),
)

LOCATION = (
    ('P', 'Portside'),
    ('S', 'Starboard Side'),
    ('F', 'Front of Ship'),
    ('BS', 'Back of Ship')
)

class Excursion(models.Model):
    activity = models.CharField(max_length=500)
    description = models.TextField(max_length=2000, default="")
    picturepath = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.activity

class Destination(models.Model):
    excursions = models.ManyToManyField(Excursion)
    location = models.CharField(max_length=250)
    description = models.TextField(max_length=3000, default="")
    picturepath = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('destinations_detail', kwargs={'pk': self.id})


class Cruise(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    sail_from = models.CharField(max_length=500)
    destinations = models.ManyToManyField(Destination)
    picturepath = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cruise_id': self.id})


class Booking(models.Model):
    price = models.IntegerField()
    date = models.DateField(("Date"), default=datetime.date.today)
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'booking_id': self.id})


# class User(models.Model):
#     username = models.CharField(max_length=25)
#     password = models.CharField(max_length=50)
#     email = models.TextField()
#     first_name = models.TextField()
#     last_name = models.TextField()
class Room(models.Model):
    type = models.CharField(
        max_length=50,
        choices=TYPE,
        default=TYPE[0][0],
    )
    cabin_number = models.IntegerField(
        default=100,
        validators=[
            MaxValueValidator(500),
            MinValueValidator(100)
        ]
    )

    location = models.CharField(
        max_length=50,
        choices=LOCATION,
        default=LOCATION[0][0]
    )

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} Cabin Number: {self.cabin_number} Price: {self.price}"
