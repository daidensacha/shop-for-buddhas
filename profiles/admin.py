from django.contrib import admin
from .models import UserProfile, Contact

# admin.site.register(Contact)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """User Profile Admin"""


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
