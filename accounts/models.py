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
    """Create AbstractUser model class for the user registration form."""
    username = models.CharField(
        verbose_name='Username',
        max_length=40,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Email Address',
        unique=True,
    )

    """Add user_type field to user profile model"""
    user_type = models.CharField(max_length=25, choices=user_type, blank=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
