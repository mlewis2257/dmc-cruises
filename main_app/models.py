from django.db import models

# Create your models here.

class Cruise(models.Model):
    name = models.CharField()
    duration = models.IntegerField()
    sale_from = models.CharField()
    destinations = models.ManyToManyField(Destination)