from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Product, Category


class UserTypeFilter(SimpleListFilter):
    title = 'User Type Filter'
    parameter_name = 'created_by_user_type'

    def lookups(self, request, model_admin):
        return (
            ('is_vendor', 'is_vendor'),
            ('vendor_username', 'vendor_username')
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'is_vendor':
            return queryset.exclude(created_by__user_type='is_customer').filter(created_by__user_type='vendor_username')
            # return queryset.exclude(created_by__user_type='is_customer')
        if self.value().lower() == 'not_vendor':
            return queryset.filter(created_by__user_type='not_vendor')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Register the Product admin view and required layout of fields"""

    fields = (
        'created_by',
        'sku',
        'name',
        'description',
        'size',
        'color',
        'price',
        'rating',
        'image_url',
        'image',
        )

    list_display = (
        'id',
        'sku',
        'name',
        'category',
        'price',
        'created_by',
        'user_type',
    )
    list_filter = ('created_by', 'category', UserTypeFilter)
    ordering = ('created_by', 'category', 'name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Register the Product Category admin view and required layout of fields
    """

    list_display = (
        'friendly_name',
        'name',
    )
