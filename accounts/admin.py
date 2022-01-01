"""
Remove unrequired apps from the admin panel by unregistering them.
Create custom layout of required form elements and information in the
accounts app in the admin panel.
"""

from django.contrib import admin
from django.contrib.auth.models import Group
# from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
from .models import UserModel

admin.site.unregister(Group)
# admin.site.register(Group)
# admin.site.unregister(Site)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    """Change layout of required information in accounts admin panel."""
    fields = (
        'first_name',
        'last_name',
        'username',
        'email',
        'password',
        'user_type',
        'date_joined',
        ('is_active', 'is_superuser')
        )
    list_display = (
        'username', 'email', 'user_type', 'date_joined', 'is_active')
    list_filter = ('user_type',)
    ordering = ('user_type', 'username',)
    search_fields = ('username', 'email', 'user_type')
    readonly_fields = ['password']
