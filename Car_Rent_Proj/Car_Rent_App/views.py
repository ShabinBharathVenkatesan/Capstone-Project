from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Booking, Reservation, Cancellation, Availability
from datetime import datetime

def calculate_price(price_per_day, pickup_date, return_date):
    # Convert string dates to datetime objects
    pickup_date = datetime.strptime(pickup_date, '%Y-%m-%d')
    return_date = datetime.strptime(return_date, '%Y-%m-%d')

    # Calculate the number of days between pickup and return
    rental_days = (return_date - pickup_date).days

    # Ensure rental days are positive
    if rental_days < 0:
        return 0  # Or raise an exception as needed

    # Calculate total price
    total_price = rental_days * price_per_day
    return total_price


def car_list(request):
    cars = Car.objects.filter(availability_status=True)
    return render(request, 'cars/car_list.html', {'cars': cars})

def book_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == "POST":
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')
        total_price = calculate_price(car.price_per_day, pickup_date, return_date)  # Define this function based on your pricing logic

        booking = Booking.objects.create(
            user=request.user,
            car=car,
            pickup_date=pickup_date,
            return_date=return_date,
            total_price=total_price,
        )
        return redirect('booking_confirmation', booking_id=booking.booking_id)

    return render(request, 'cars/book_car.html', {'car': car})

def reserve_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == "POST":
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')

        reservation = Reservation.objects.create(
            user=request.user,
            car=car,
            pickup_date=pickup_date,
            return_date=return_date,
        )
        return redirect('reservation_confirmation', reservation_id=reservation.reservation_id)

    return render(request, 'cars/reserve_car.html', {'car': car})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        reason = request.POST.get('reason')
        Cancellation.objects.create(booking=booking, reason=reason)
        booking.delete()  # Optionally delete the booking or mark it as cancelled
        return redirect('profile')  # Redirect to user profile or bookings page

    return render(request, 'cancel_booking.html', {'booking': booking})

def check_availability(request):
    if request.method == "POST":
        car_id = request.POST.get('car_id')
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')

        available_quantity = check_car_availability(car_id, pickup_date, return_date)

        return render(request, 'availability_result.html', {'available_quantity': available_quantity})

    return render(request, 'check_availability.html')

def check_car_availability(car_id, pickup_date, return_date):
    # Check if there are any overlapping bookings
    has_bookings = Booking.objects.filter(
        car_id=car_id,
        pickup_date__lt=return_date,
        return_date__gt=pickup_date
    ).exists()

    # Get the availability record for the car
    availability_record = Availability.objects.filter(car__car_id=car_id).first()

    if availability_record:
        if has_bookings:
            return max(0, availability_record.available_quantity - 1)  # Reduce by one if booked
        return availability_record.available_quantity  # Return full quantity if no bookings

    return 0  # If no availability record exists
