from django.urls import path
from .views import (
    car_list,
    book_car,
    reserve_car,
    cancel_booking,
    check_availability
)

urlpatterns = [
    path('', car_list, name='car_list'),
    path('car/<int:car_id>/book/', book_car, name='book_car'),
    path('car/<int:car_id>/reserve/', reserve_car, name='reserve_car'),
    path('cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('check_availability/', check_availability, name='check_availability'),
]
