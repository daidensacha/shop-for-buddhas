from django.urls import path
from .views import blog_posts, post_detail, post_archive_month, blog_search

urlpatterns = [
    path('', blog_posts, name='blog_posts'),
    path('search/', blog_search, name='blog_search'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', blog_posts, name='post_tag'),
    path('category/<slug:category_slug>/', blog_posts, name='post_category'),
    path('post_archive_month/<year>/<month>/', post_archive_month,
         name='post_archive_month'),

]
