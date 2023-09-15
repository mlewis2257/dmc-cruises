from django.db import models

# Create your models here.

class Destination(models.Model):
    excursions = models.CharField()
    location = models.CharField()
    

class Cruise(models.Model):
    name = models.CharField()
    duration = models.IntegerField()
    sale_from = models.CharField()
    destinations = models.ManyToManyField(Destination)

    def __str__(self):
        return f'{self.name} ({self.id})'