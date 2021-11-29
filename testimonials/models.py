from django.db import models
# from django.contrib.auth.models import User
from accounts.models import Profile
from datetime import datetime


rating = (("1", "1/5 stars"),
          ("2", "2/5 stars"),
          ("3", "3/5 stars"),
          ("4", "4/5 stars"),
          ("5", "5/5 stars")
        )


class Testimonial(models.Model):
    """Create testimonial class model"""
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user_image = models.ImageField()
    user_testimonial = models.TextField(max_length=254)
    user_rating = models.CharField(max_length=150, choices=rating)
    posted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
