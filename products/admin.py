from django.contrib import admin
from .models import Product, Category
from accounts.models import UserModel


class VendorFilter(admin.SimpleListFilter):
    """Return list of vendors for Product admin"""
    title = "Vendors"
    parameter_name = "vendor"

    def lookups(self, request, model_admin):
        vendor_list = []
        users = UserModel.objects.all()
        for user in users:
            product = Product.objects.filter(created_by=user)
            if product:
                vendor_list.append((user, user))
        return vendor_list

    def queryset(self, request, queryset):
        if not self.value():
            return queryset.all()
        return queryset.filter(created_by__username=self.value())


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Register the Product admin view and required layout of fields"""

    fields = (
        'created_by',
        'category',
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
    list_filter = (VendorFilter, 'category', )
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
