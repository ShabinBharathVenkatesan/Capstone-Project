# from django.urls import path
# from .views import admin_user_list, create_admin_user, edit_admin_user

# urlpatterns = [
#     path('admins/', admin_user_list, name='admin_user_list'),
#     path('admins/create/', create_admin_user, name='create_admin_user'),
#     path('admins/edit/<int:user_id>/', edit_admin_user, name='edit_admin_user'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminUserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'admin_users', AdminUserViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs for admin user management API
]
