"""Register the name of the accounts app"""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Add verbose name to change name of App in Admin panel."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = "Accounts Users"
