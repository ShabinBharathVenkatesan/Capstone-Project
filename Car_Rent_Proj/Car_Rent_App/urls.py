

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, BookingViewSet, ReservationViewSet, CancellationViewSet, AvailabilityViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'cancellations', CancellationViewSet)
router.register(r'cars/availability', AvailabilityViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs for REST API
]
