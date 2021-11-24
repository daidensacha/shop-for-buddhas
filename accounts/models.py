"""
Create custom AbstractUser model for allauth signup form
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

user_type = (
    ('is_admin', "Admin"),
    ('is_customer', "Customer"),
    ('is_vendor', "Vendor")
)

# Can I change this from Profile to CustomUserProfile?


class Profile(AbstractUser):
    """Add user_type field to user profile model"""
    user_type = models.CharField(max_length=25, choices=user_type, blank=True)
