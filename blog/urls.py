from django.urls import path
from .views import blog_posts, post_detail

urlpatterns = [
    path("", blog_posts, name="blog_posts"),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', blog_posts, name='post_tag'),
    path('category/<slug:category_slug>/', blog_posts, name='post_category'),
]
