

from django.db import models
from django.contrib.auth.models import User
class AdminUser(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Username field
    password = models.CharField(max_length=128)  # Password field

    def __str__(self):
        return self.username

# class AdminUser(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128, default="temporary_password")  # Add default
