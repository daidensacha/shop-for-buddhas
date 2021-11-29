from django.db import models
# from django.contrib.auth.models import User
from accounts.models import Profile
# Create your models here.


class Testimonial(models.Model):
    """Create testimonial class model"""
    # user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user_image = models.ImageField()
    # increase length of the testimonial to 200 character TEXTAREA
    # user_testimonial = models.CharField(
    #                       max_length=150, widget=forms.Textarea)
    # or user_testimonial = models.TextField(max_length=254)
    user_testimonial = models.CharField(max_length=150)
    user_rating = models.CharField(max_length=150)
    posted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
        # instance of 'ForeignKey' has no 'username' member?
        # Why is the user showing as email, not PK integer?
