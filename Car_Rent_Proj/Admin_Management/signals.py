from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import AdminUser

@receiver(post_save, sender=User)
def create_admin_user(sender, instance, created, **kwargs):
    if created:
        AdminUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_admin_user(sender, instance, **kwargs):
    instance.adminuser.save()
