from django.contrib import admin
from .models import Cruise, Destination, Booking, Room, User, Excursion

# Register your models here.
admin.site.register(Cruise)
admin.site.register(Destination)
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(Excursion)
# admin.site.register(User)
