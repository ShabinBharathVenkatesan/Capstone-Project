"""
URL configuration for Car_Rent_Proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# from django.contrib import admin
# from django.urls import path, include
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Car Rent API",
#       default_version='v1',
#       description="API documentation for Car Rental application",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@carrent.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('cars/', include('Car_Rent_App.urls')),  # Include URLs from Car_Rent_App
#     path('user/', include('User_Management.urls')),  # Include URLs from User_Management
#     path('admin_management/', include('Admin_Management.urls')),  # Include URLs from Admin_Management
    
#     # Swagger UI and Schema endpoints
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]


from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt import authentication
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Set up Swagger schema view
schema_view = get_schema_view(
   openapi.Info(
      title="Car Rent API",
      default_version='v1',
      description="API documentation for the Car Rental application",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@carrent.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   authentication_classes=(authentication.JWTAuthentication,),
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Include URLs for Car_Rent_App
    path("api/cars/", include('Car_Rent_App.urls')),  # Adjusted to match your app structure

    # Include URLs for User Management and Admin Management if applicable
    path("api/user/", include('User_Management.urls')),
    path("api/admin/", include('Admin_Management.urls')),  # If you have admin management

    # Swagger documentation endpoint
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# Serve static files in development (if needed)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from rest_framework_simplejwt import authentication
# from django.urls import path, include
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from Admin_Management.schema_generator import CustomSchemaGenerator  # Import your custom generator

# # Set up Swagger schema view
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Car Rent API",
#       default_version='v1',
#       description="API documentation for the Car Rental application",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@carrent.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    authentication_classes=(authentication.JWTAuthentication,),
#    permission_classes=(permissions.AllowAny,),
#    generator_class=CustomSchemaGenerator # Use your custom generator
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # JWT Token endpoints
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     # Include URLs for Car_Rent_App
#     path("api/cars/", include('Car_Rent_App.urls')),  # Adjusted to match your app structure

#     # Include URLs for User Management and Admin Management if applicable
#     path("api/user/", include('User_Management.urls')),
#     path("api/admin/", include('Admin_Management.urls')),  # If you have admin management

#     # Swagger documentation endpoint
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
# ]
