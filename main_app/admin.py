from django.contrib import admin
from .models import Cruise, Destination, Booking, Room, User

# Register your models here.
admin.site.register(Cruise)
admin.site.register(Destination)
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(User)
