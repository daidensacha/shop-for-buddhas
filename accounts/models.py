from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
user_type = (
    ('customer', "Customer"),
    ('vendor', "Vendor")
)


class Profile(AbstractUser):
    user_type = models.CharField(max_length=25, choices=user_type)
