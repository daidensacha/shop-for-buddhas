from django.contrib import admin
from .models import UserProfile, Contact


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    User Profile Admin
    Change the user field to read only
    """
    readonly_fields = ('user',)
    fields = (
        'user',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode',
        'default_country',
        'default_user_bio',
        )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Contact Admin"""
    readonly_fields = ('date_sent',)
    fields = (
        'date_sent',
        'first_name',
        'last_name',
        'sender',
        'subject',
        'message',
        )
    list_display = (
        'date_sent', 'first_name', 'last_name', 'sender', 'subject',
    )
    ordering = ('-date_sent', 'first_name', 'last_name',)
