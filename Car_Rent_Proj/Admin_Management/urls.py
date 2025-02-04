from django.urls import path
from .views import admin_user_list, create_admin_user, edit_admin_user

urlpatterns = [
    path('admins/', admin_user_list, name='admin_user_list'),
    path('admins/create/', create_admin_user, name='create_admin_user'),
    path('admins/edit/<int:user_id>/', edit_admin_user, name='edit_admin_user'),
]
