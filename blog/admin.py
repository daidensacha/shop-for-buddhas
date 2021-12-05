from django.contrib import admin
from .models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Change layout of required information in accounts admin panel."""

    prepopulated_fields = {"slug": ("title",)}
    fields = (
              'author',
              'category',
              'title',
              'slug',
              'image',
              'tags',
              'description',
              'body',
              'created_at',
              'posted_at'
             )
    list_display = ('title', 'category', 'author', 'created_at', 'posted_at')
    list_filter = ('category', 'tags')
    ordering = ('created_at',)


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
