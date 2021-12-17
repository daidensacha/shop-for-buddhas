from django.contrib import admin
from .models import UserProfile
# Register your models here.
# admin.site.register(UserProfile)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Change layout of required information in accounts admin panel."""
    # fields = (
    #     'first_name',
    #     'last_name',
    #     'username',
    #     'email',
    #     'password',
    #     'user_type',
    #     'date_joined',
    #     ('is_active', 'is_superuser')
    #     )
    # list_display = ('username', 'user_type', 'date_joined')
    # list_filter = ('user_type',)
    # ordering = ('user_type', 'username',)
    # search_fields = ('username', 'email', 'user_type')
    # readonly_fields = ['password']


# @admin.register(UserModel)
# class UserModelAdmin(admin.ModelAdmin):
#     """Change layout of required information in accounts admin panel."""
#     fields = (
#         'first_name',
#         'last_name',
#         'username',
#         'email',
#         'password',
#         'user_type',
#         'date_joined',
#         ('is_active', 'is_superuser')
#         )
#     list_display = ('username', 'email', 'user_type', 'date_joined')
#     list_filter = ('user_type',)
#     ordering = ('user_type', 'username',)
#     search_fields = ('username', 'email', 'user_type')
#     readonly_fields = ['password']