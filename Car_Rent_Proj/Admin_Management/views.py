

# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from .models import AdminUser
# from .serializers import AdminUserSerializer  # Ensure this serializer is defined

# class AdminUserViewSet(viewsets.ModelViewSet):
#     queryset = AdminUser.objects.all()
#     serializer_class = AdminUserSerializer
#     authentication_classes = [JWTAuthentication]  # Use JWT Authentication
#     permission_classes = [IsAuthenticated]  # Ensure this matches your requirements

#     def list(self, request):
#         return super().list(request)

#     def create(self, request):
#         return super().create(request)


# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from .models import AdminUser
# from .serializers import AdminUserSerializer

# class AdminUserViewSet(viewsets.ModelViewSet):
#     queryset = AdminUser.objects.all()
#     serializer_class = AdminUserSerializer
#     authentication_classes = [JWTAuthentication]  # Use JWT Authentication
#     permission_classes = [IsAuthenticated]  # Ensure this matches your requirements



from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import AdminUser
from .serializers import AdminUserSerializer

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [IsAuthenticated]  # Ensure this matches your requirements

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

