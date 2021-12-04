from django.shortcuts import render
from .models import Category, Blog, Comment
# Create your views here.


def blog_detail(request):
    blog = Blog.objects.all()
    category = Category.objects.all()

    context = {
        "blog": blog,
        "category": category,
    }

    return render(request, "blog/blog_list.html", context)
