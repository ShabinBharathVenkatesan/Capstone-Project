from django.contrib import admin
from .models import Car, Booking, Reservation, Cancellation, Availability

admin.site.register(Car)
admin.site.register(Booking)
admin.site.register(Reservation)
admin.site.register(Cancellation)
admin.site.register(Availability)
