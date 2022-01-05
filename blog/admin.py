from django.contrib import admin
from .models import Category, Post, Comment
from taggit.admin import Tag


admin.site.unregister(Tag)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Prepopulate the slug field in the admin view"""

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Change layout of required information in accounts admin panel. """

    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)
    fields = (
              'author',
              'category',
              'title',
              'slug',
              'image',
              'tags',
              'description',
              'body',
              'status',
              'featured',
              'created_at',
              'posted_at'
             )
    list_display = ('title', 'category', 'author', 'featured', 'status',
                    'created_at', 'posted_at')
    list_filter = ('category', 'tags')
    ordering = ('created_at',)


# admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Comment Admin Layout """

    readonly_fields = ('posted_by', 'created_at')
    fields = (
        'post',
        'name',
        'body',
        'posted_by',
        'created_at'
    )
    list_display = (
        'created_at',
        'posted_by',
        'name',
        'post'
    )
    list_filter = ('posted_by', 'name',)
    ordering = ('created_at', 'posted_by',)
