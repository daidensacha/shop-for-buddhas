"""
Customise the admin view of the Testimonial app
"""
from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """Change layout of required information in testimonial admin panel."""
    readonly_fields = ('created_at',)
    fields = (
        'user',
        'image',
        'user_testimonial',
        'user_rating',
        'approved',
        'created_at',
        'posted_at'
        )

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'Username'
    get_username.admin_order_field = 'user'
    list_display = ('get_username', 'created_at', 'approved', 'posted_at')
    list_filter = ('approved',)
    ordering = ('-created_at',)
