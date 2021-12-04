from django.urls import path
from .views import blog_detail

urlpatterns = [
    path("", blog_detail, name="blog_list"),
]
