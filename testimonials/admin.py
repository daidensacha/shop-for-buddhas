"""
Customise the admin view of the Testimonial app
"""
from django.contrib import admin
from .models import Testimonial
# Register your models here.
# admin.site.register(Testimonial)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """Change layout of required information in testimonial admin panel."""
    fields = (
        # Why is user showing as email? Would prefer username
        'user',
        # 'user_email',
        # Cannot show the username???
        # 'username',
        'user_image',
        'user_testimonial',
        'user_rating',
        # Cannot show the created_at field in the form???
        'created_at',
        'approved',
        'posted_at'
        )
    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = "Username"
    get_username.admin_order_field = "user"
    # Cannot show the username in the list_display???
    list_display = ('get_username', 'created_at', 'approved', 'posted_at')
    list_filter = ('approved',)
    ordering = ('created_at',)
    # search_fields = ('username', 'email', 'user_type')
    # readonly_fields = ['password']
