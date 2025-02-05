# from django.urls import path
# from .views import profile_view, edit_profile, create_user_profile

# urlpatterns = [
#     path('profile/', profile_view, name='profile_view'),
#     path('profile/edit/', edit_profile, name='edit_profile'),
#     path('profile/create/', create_user_profile, name='create_user_profile'),
# ]


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserProfileViewSet

# router = DefaultRouter()
# router.register(r'profiles', UserProfileViewSet)

# urlpatterns = [
#     path('', include(router.urls)),  # Include the router URLs
# ]

# urls.py

from django.urls import path
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]
