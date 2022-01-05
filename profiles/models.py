from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib import auth
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile',
        on_delete=models.CASCADE,)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)
    default_user_bio = models.CharField(
        max_length=300, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=auth.get_user_model())
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        instance.profile.save()


class Contact(models.Model):
    """ Create a contact form model """
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    subject = models.CharField(max_length=25)
    sender = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        verbose_name = "Message"

    def __str__(self):
        return self.first_name+self.last_name
