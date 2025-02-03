from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=15, unique=True)
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    pickup_date = models.DateField()
    return_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    pickup_date = models.DateField()
    return_date = models.DateField()

class Cancellation(models.Model):
    cancellation_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    cancellation_date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

class Availability(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True)
    pickup_date = models.DateField()
    return_date = models.DateField()
    available_quantity = models.IntegerField()
