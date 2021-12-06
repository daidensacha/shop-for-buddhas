from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'size',
        'color',
        'price',
        'rating',
        'image',
    )
    list_filter = ('category',)
    ordering = ('category', 'sku',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)
