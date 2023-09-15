from django.db import models
from django.urls import reverse

# Create your models here.

ROOM_TYPE = (
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
    ('BS'. 'Back of Ship')
)


class Destination(models.Model):
    excursions = models.CharField(max_length=500)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('destinations_detail', kwargs={'pk': self.id})

    

class Cruise(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    sale_from = models.CharField(max_length=500)
    destinations = models.ManyToManyField(Destination)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cruise_id': self.id})

class Room(models.Model):
    type = models.CharField(
        max_length=50,
        choices=ROOM_TYPE,
        default=ROOM_TYPE[0][0],
    )
    number = models.IntegerField(
        min_num=100,
        max_num=500
    )
    location = models.CharField(
        max_length=50,
        choices=LOCATION,
        default=LOCATION[0][0]
        )

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_room_display()} on {self.date}"

class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    email = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()


class Booking(models.Model):
    cruises = models.OneToManyField(cruise)
    users = models.OneToManyField(user)
    destinations = models.ManyToManyField(destination)
    price = models.IntegerField()