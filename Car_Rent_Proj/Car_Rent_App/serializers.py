from rest_framework import serializers
from .models import Car, Booking, Reservation, Cancellation, Availability


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class CancellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancellation
        fields = ['booking', 'reason']

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['car', 'pickup_date', 'return_date', 'available_quantity']  # Adjust fields as necessary

class CarAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['car', 'pickup_date', 'return_date', 'available_quantity']