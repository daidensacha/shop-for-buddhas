from django.db import models
from accounts.models import Profile
# Create your models here.


class Testimonial(models.Model):
    """Create testimonial class model"""
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user_image = models.ImageField()
    user_testimonial = models.CharField(max_length=150)
    user_rating = models.CharField(max_length=150)
    posted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
        # instance of 'ForeignKey' has no 'username' member?
