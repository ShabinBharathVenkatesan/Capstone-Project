from django.db import models
from django.contrib.auth.models import User

class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to User model
    # Add any additional fields if necessary
    is_super_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
