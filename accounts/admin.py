from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User, Group
# from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken

# Register your models here.

# admin.site.register(Profile)
admin.site.unregister(Group)
# admin.site.unregister(Site)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
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
    list_display = ('username', 'email', 'user_type', 'date_joined')
    list_filter = ('user_type',)
    ordering = ('username',)
    search_fields = ('username', 'email', 'user_type')
