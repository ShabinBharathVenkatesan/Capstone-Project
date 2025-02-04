from django.urls import path
from .views import profile_view, edit_profile, create_user_profile

urlpatterns = [
    path('profile/', profile_view, name='profile_view'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/create/', create_user_profile, name='create_user_profile'),
]
