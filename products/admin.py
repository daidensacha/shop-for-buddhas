from django.contrib import admin
from .models import Product, Category


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
        'created_by',
        'sku',
        'name',
        'category',
        'price',
    )
    list_filter = ('created_by', 'category',)
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
