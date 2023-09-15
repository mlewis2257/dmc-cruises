from django.db import models
from django.urls import reverse

# Create your models here.

class Destination(models.Model):
    excursions = models.CharField(max_length=500)
    location = models.CharField(max_length=250)
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE)

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

class Room(model.Models):
    type = models.TextField()
    number = models.IntegerField()
    location = models.TextField()
    booking = models.ForeignKey(Room, on_delete=models.CASCADE)


class User(model.Models):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    email = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()


class Booking(model.Models):
    cruises = models.OneToManyField(cruise)
    users = models.OneToManyField(user)
    destinations = models.ManyToManyField(destination)
    rooms = models.OneToManyField(room)
    price = models.IntegerField()