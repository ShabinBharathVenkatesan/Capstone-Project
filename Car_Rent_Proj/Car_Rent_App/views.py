# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from .models import Car, Booking, Reservation, Cancellation, Availability
# from .serializers import CarSerializer, BookingSerializer, ReservationSerializer, CancellationSerializer, AvailabilitySerializer, CarAvailabilitySerializer

# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import action
# class CarViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     authentication_classes = [JWTAuthentication]  # Use JWT Authentication
#     permission_classes = [IsAuthenticated]  # Ensure this matches your requirements

#     def list(self, request):
#         return super().list(request)

# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#     authentication_classes = [JWTAuthentication]  # Use JWT Authentication
#     permission_classes = [IsAuthenticated]

#     def create(self, request):
#         return super().create(request)

# class ReservationViewSet(viewsets.ModelViewSet):
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer
#     authentication_classes = [JWTAuthentication]  # Use JWT Authentication
#     permission_classes = [IsAuthenticated]

#     def create(self, request):
#         return super().create(request)

# class CancellationViewSet(viewsets.ModelViewSet):
#     queryset = Cancellation.objects.all()
#     serializer_class = CancellationSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def create(self, request):
#         booking_id = request.data.get('booking')  # Use 'booking' from request data (assuming your serializer uses 'booking')
#         reason = request.data.get('reason')

#         # Check if the booking exists
#         try:
#             booking = Booking.objects.get(booking_id=booking_id)  # Use booking_id here
#             cancellation = Cancellation.objects.create(booking=booking, reason=reason)
#             return Response(CancellationSerializer(cancellation).data, status=status.HTTP_201_CREATED)
#         except Booking.DoesNotExist:
#             return Response({"error": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)
        
      


# class AvailabilityViewSet(viewsets.ModelViewSet):
#     queryset = Availability.objects.all()
#     serializer_class = AvailabilitySerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     @action(detail=False, methods=['get'], url_path='check')
#     def check_availability(self, request):
#         car_id = request.query_params.get('car_id')
#         pickup_date = request.query_params.get('pickup_date')
#         return_date = request.query_params.get('return_date')

#         if not car_id or not pickup_date or not return_date:
#             return Response({"error": "Missing required parameters."}, status=status.HTTP_400_BAD_REQUEST)

#         # Check availability logic
#         available_quantity = self.get_availability(car_id, pickup_date, return_date)

#         # Get the availability record for the car
#         availability_record = self.get_queryset().filter(car__car_id=car_id).first()

#         if availability_record:
#             # Return the available quantity along with existing availability details
#             serialized_availability = AvailabilitySerializer(availability_record).data
#             serialized_availability['available_quantity'] = available_quantity  # Add available quantity to the serialized data
#             return Response(serialized_availability)

#         return Response({"available_quantity": available_quantity})  # If no availability record exists

#     def get_availability(self, car_id, pickup_date, return_date):
#         # Count bookings that overlap with the requested dates
#         bookings_count = Booking.objects.filter(
#             car_id=car_id,
#             pickup_date__lt=return_date,
#             return_date__gt=pickup_date
#         ).count()

#         # Get the availability record for the car
#         availability_record = Availability.objects.filter(car__car_id=car_id).first()

#         if availability_record:
#             available_quantity_after_bookings = availability_record.available_quantity - bookings_count
#             return max(0, available_quantity_after_bookings)  # Ensure we don't go below zero

#         return 0  # If no availability record exists
    


# class AvailabilityViewSet(viewsets.ModelViewSet):
#     queryset = Availability.objects.all()
#     serializer_class = AvailabilitySerializer  # Set the serializer to CarAvailabilitySerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         serializer = CarAvailabilitySerializer(data=request.data)  # Use the CarAvailabilitySerializer
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Car, Booking, Reservation, Cancellation, Availability
from .serializers import CarSerializer, BookingSerializer, ReservationSerializer, CancellationSerializer, AvailabilitySerializer, CarAvailabilitySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]  # Ensure this matches your requirements

    def list(self, request):
        return super().list(request)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]

    def create(self, request):
        return super().create(request)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]

    def create(self, request):
        return super().create(request)


class CancellationViewSet(viewsets.ModelViewSet):
    queryset = Cancellation.objects.all()
    serializer_class = CancellationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        booking_id = request.data.get('booking')  # Use 'booking' from request data (assuming your serializer uses 'booking')
        reason = request.data.get('reason')

        # Check if the booking exists
        try:
            booking = Booking.objects.get(booking_id=booking_id)  # Use booking_id here
            cancellation = Cancellation.objects.create(booking=booking, reason=reason)
            return Response(CancellationSerializer(cancellation).data, status=status.HTTP_201_CREATED)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)
        


class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='check')
    def check_availability(self, request):
        car_id = request.query_params.get('car') #Get the car id
        pickup_date = request.query_params.get('pickup_date')
        return_date = request.query_params.get('return_date')

        if not car_id or not pickup_date or not return_date:
            return Response({"error": "Missing required parameters."}, status=status.HTTP_400_BAD_REQUEST)

        # Check availability logic
        available_quantity = self.get_availability(car_id, pickup_date, return_date)

        # Get the availability record for the car
        availability_record = self.get_queryset().filter(car_id=car_id).first() #Get it by car ID

        if availability_record:
            # Return the available quantity along with existing availability details
            serialized_availability = AvailabilitySerializer(availability_record).data
            serialized_availability['available_quantity'] = available_quantity  # Add available quantity to the serialized data
            return Response(serialized_availability)

        return Response({"available_quantity": available_quantity})  # If no availability record exists

    def get_availability(self, car_id, pickup_date, return_date):
        # Count bookings that overlap with the requested dates
        bookings_count = Booking.objects.filter(
            car_id=car_id,
            pickup_date__lt=return_date,
            return_date__gt=pickup_date
        ).count()

        # Get the availability record for the car
        availability_record = Availability.objects.filter(car_id=car_id).first()#Get it by car ID

        if availability_record:
            available_quantity_after_bookings = availability_record.available_quantity - bookings_count
            return max(0, available_quantity_after_bookings)  # Ensure we don't go below zero

        return 0  # If no availability record exists
